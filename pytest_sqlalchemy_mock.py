from typing import TYPE_CHECKING

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


@pytest.fixture(scope="session")
def connection_url():
    return "sqlite:///:memory:"


@pytest.fixture(scope="function")
def engine(connection_url):
    return create_engine(connection_url)


@pytest.fixture(scope="function")
def connection(engine):
    return engine.connect()


@pytest.fixture(scope="function")
def session(connection):
    session: Session = sessionmaker()(bind=connection)
    yield session
    session.close()
