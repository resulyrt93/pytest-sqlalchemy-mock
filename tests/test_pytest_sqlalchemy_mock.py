from sqlalchemy import text

from .data import MockData
from .db import (
    Department,
    User,
)


def test_get_session(session):
    assert session.execute(text("SELECT 5")).scalar() == 5


def test_session_user_table(session):
    assert session.execute(text("SELECT count(*) from user")).scalar() == 0


def test_session_query_for_assocation_table(session):
    assert session.execute(text("SELECT count(*) from user_department")).scalar() == 0


def test_mocked_session_user_table(mocked_session):
    user_data = mocked_session.execute(text("SELECT * from user;")).first()
    raw_data = MockData.USER_DATA[0]
    assert user_data[0] == raw_data["id"]
    assert user_data[1] == raw_data["name"]
    assert user_data[2] == raw_data["surname"]
    assert user_data[3] == raw_data["is_admin"]
    assert user_data[4] == raw_data["city"]


def test_mocked_session_user_model(mocked_session):
    user = mocked_session.query(User).filter_by(id=2).first()
    raw_data = MockData.USER_DATA[1]
    assert user.name == raw_data["name"]
    assert user.is_admin == raw_data["is_admin"]
    assert user.departments[0].name == "Sales"


def test_mocked_session_department_model(mocked_session):
    department = mocked_session.query(Department).filter_by(id=1).first()
    raw_data = MockData.DEPARTMENT_DATA[0]
    assert department.name == raw_data["name"]
    assert len(department.users) == 1
    assert department.users[0].name == "Kevin"
