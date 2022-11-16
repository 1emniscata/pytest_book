from collections import namedtuple
# from tasks import TasksException
from src.tasks import Task
# Task = namedtuple("Task", ["summary", "owner", "done", "id"])
# Task.__new__.__defaults__ = (None, None, False, None)


def test_task_equality():
    t1 = Task("sit there", "Brian")
    t2 = Task("do smth", "Okken")
    assert t1 == t2

def test_dict_equality():
    t1_dict = Task("do sandwich", "Okken")._asdict()
    t2_dict = Task("do sandwich", "Okkem")._asdict()
    assert t1_dict == t2_dict
