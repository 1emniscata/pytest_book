import pytest
import src.tasks as tasks
from src.tasks import Task


def test_add_returns_valid_id():
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    new_task = Task("do smth")
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    new_task = Task("sit in chair", owner="me", done=True)
    task_id = tasks.add(new_task)
    task_from_db = tasks.get(task_id)
    assert task_from_db.id == task_id

@pytest.mark.xfail(reason="Fixture has only 3 tasks")
def test_add_increases_count(db_with_3_tasks):
    # GIVEN a db with 3 tasks
    # WHEN another task is added
    tasks.add(Task("throw a party"))
    # THEN the count increases by 1
    assert tasks.count() == 4
