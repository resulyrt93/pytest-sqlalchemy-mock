from typing import TYPE_CHECKING

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .model_mocker import ModelMocker

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


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
