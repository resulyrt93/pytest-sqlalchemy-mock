import pytest

from pytest_sqlalchemy_mock import *
from tests.data import MockData
from tests.db import Base


@pytest.fixture(scope="function")
def sqlalchemy_declarative_base():
    return Base


@pytest.fixture(scope="function")
def sqlalchemy_mock_config():
    return [("user", MockData.USER_DATA)]
