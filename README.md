# pytest-sqlalchemy-mock  👋
[![PyPI version](https://badge.fury.io/py/pytest-sqlalchemy-mock.svg)](https://badge.fury.io/py/pytest-sqlalchemy-mock)
[![codecov](https://codecov.io/gh/resulyrt93/pytest-sqlalchemy-mock/branch/dev/graph/badge.svg?token=RUQ4DN3CH9)](https://codecov.io/gh/resulyrt93/pytest-sqlalchemy-mock)
[![CI](https://github.com/resulyrt93/pytest-sqlalchemy-mock/actions/workflows/tests.yaml/badge.svg?branch=dev)](https://github.com/resulyrt93/pytest-sqlalchemy-mock/actions/workflows/tests.yaml)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/pytest-sqlalchemy-mock)](https://github.com/resulyrt93/pytest-sqlalchemy-mock)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

This plugin provides pytest fixtures to create an in-memory DB instance on tests and dump your raw test data.

## Installation
```
pip install pytest-sqlalchemy-mock
```

## Usage
Let's assume you have a SQLAlchemy declarative base and some models with it.

**models.py**
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
```
Firstly SQLAlchemy base class which is used for declare models should be passed with `sqlalchemy_declarative_base` fixture in `conftest.py`

**conftest.py**
```python
@pytest.fixture(scope="function")
def sqlalchemy_declarative_base():
    return Base
```
Then in test functions you can use `mocked_session` fixture to make query in mocked DB.

**test_user_table.py**
```python
def test_mocked_session_user_table(mocked_session):
    user_data = mocked_session.execute("SELECT * from user;").all()
    assert user_data == []
```
Also, you can dump your mock data to DB before start testing via `sqlalchemy_mock_config` fixture like following.

**conftest.py**
```python
@pytest.fixture(scope="function")
def sqlalchemy_mock_config():
    return [("user", [
        {
            "id": 1,
            "name": "Kevin"
        },
        {
            "id": 2,
            "name": "Dwight"
        }
    ])]
```
**test_user_table.py**
```python
def test_mocked_session_user_class(mocked_session):
    user = mocked_session.query(User).filter_by(id=2).first()
    assert user.name == "Dwight"
```

## Upcoming Features
* Mock with decorator for specific DB states for specific cases.
* Support to load data from `.json` and `.csv`
* Async SQLAlchemy support
