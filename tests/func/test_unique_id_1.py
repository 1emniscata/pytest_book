import pytest

from src import tasks
from src.tasks import Task


@pytest.mark.xfail(
    tasks.__version__ < "0.2.0",
    reason="not supported until version 0.2.0"
)
def test_unique_id():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    """unique_id() should return an unused id."""

    ids = []
    ids.append(tasks.add(Task("one")))
    ids.append(tasks.add(Task("two")))
    ids.append(tasks.add(Task("three")))

    uid = tasks.unique_id()
    assert uid not in ids

@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    uid = tasks.unique_id()
    assert uid == "a duck"

@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    uid = tasks.unique_id()
    assert uid != "a duck"