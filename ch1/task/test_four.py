from collections import namedtuple

Task = namedtuple("Task", ["summary", "owner", "done", "id"])
Task.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    t_task = Task("do smth", "Okken", True, 21)
    t_dict = t_task._asdict()
    expected = {
        "summary": "do smth",
        "owner": "Okken",
        "done": True,
        "id": 21
    }
    assert t_dict == expected


def test_replace():
    t_before = Task("finish book", "Brian")
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task("finish book", "Brian", True, 10)
    assert t_after == t_expected
