from typing import TYPE_CHECKING, List, Tuple

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class ModelMocker:
    # TODO make type annotations
    _base = None
    _mock_config: List[Tuple[str, List]] = None

    def __init__(self, session, base, mock_config):
        self._session: Session = session
        self._base = base
        self._mock_config = mock_config

    def get_model_class_with_table_name(self, table_name: str):
        for mapper in self._base.registry.mappers:
            cls = mapper.class_
            if cls.__tablename__ == table_name:
                return cls

    def create_all(self):
        for model_config in self._mock_config:
            table_name, data = model_config
            model_class = self.get_model_class_with_table_name(table_name)
            if model_class:
                for datum in data:
                    instance = model_class(**datum)
                    self._session.add(instance)
        self._session.commit()


@pytest.fixture(scope="session")
def connection_url():
    return "sqlite:///:memory:"


@pytest.fixture(scope="function")
def engine(connection_url):
    return create_engine(connection_url)


@pytest.fixture(scope="function")
def sqlalchemy_declarative_base():
    return


@pytest.fixture(scope="function")
def sqlalchemy_mock_config():
    return


@pytest.fixture(scope="function")
def connection(engine, sqlalchemy_declarative_base):
    if sqlalchemy_declarative_base:
        sqlalchemy_declarative_base.metadata.create_all(engine)
    return engine.connect()


@pytest.fixture(scope="function")
def session(connection):
    session: Session = sessionmaker()(bind=connection)
    yield session
    session.close()


@pytest.fixture(scope="function")
def mocked_session(
    connection, sqlalchemy_declarative_base, sqlalchemy_mock_config
):
    session: Session = sessionmaker()(bind=connection)

    if sqlalchemy_declarative_base and sqlalchemy_mock_config:
        ModelMocker(
            session, sqlalchemy_declarative_base, sqlalchemy_mock_config
        ).create_all()

    yield session
    session.close()
