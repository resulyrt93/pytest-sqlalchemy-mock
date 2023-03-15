# TODO use pytester for testing
from pytest_sqlalchemy_mock.base import *
from tests.data import MockData
from tests.db import Base


@pytest.fixture(scope="function")
def sqlalchemy_declarative_base():
    return Base


@pytest.fixture(scope="function")
def sqlalchemy_mock_config():
    return [
        ("user", MockData.USER_DATA),
        ("department", MockData.DEPARTMENT_DATA),
        ("user_department", MockData.USER_DEPARTMENT_DATA),
    ]
