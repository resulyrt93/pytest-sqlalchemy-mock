from datetime import datetime


class MockData:
    USER_DATA = [
        {
            "id": 1,
            "name": "Kevin",
            "surname": "Malone",
            "is_admin": False,
            "city": "NY",
            "join_date": datetime(2011, 7, 27, 16, 2, 8),
        },
        {
            "id": 2,
            "name": "Dwight",
            "surname": "Schrute",
            "is_admin": True,
            "city": "PA",
            "join_date": datetime(2009, 11, 20, 21, 3, 12),
        },
    ]

    DEPARTMENT_DATA = [
        {
            "id": 1,
            "name": "Accounting",
        },
        {
            "id": 2,
            "name": "Sales",
        },
    ]

    USER_DEPARTMENT_DATA = [
        {
            "user_id": 1,
            "department_id": 1,
        },
        {
            "user_id": 2,
            "department_id": 2,
        },
    ]
