import pytest


@pytest.fixture(scope="module")
def test_data():
    return [
        {
            "name": "test_1",
            "description": "test_1",
            "tags": ["tag1", "tag2"],
            "status": "open",
            "priority": "high",
            "assigned_to": "test_user",
            "due_date": "2020-01-01",
        },
        {
            "name": "test_2",
            "description": "test_2",
            "tags": ["tag1", "tag3"],
            "status": "closed",
            "priority": "medium",
            "assigned_to": "test_user",
            "due_date": "2020-01-01",
        },
        {
            "name": "test_3",
            "description": "test_3",
            "tags": ["tag1", "tag2"],
            "status": "open",
            "priority": "low",
            "assigned_to": "test_user",
            "due_date": "2020-01-01",
        },
    ]