import pytest

from src import tasks
from src.tasks import Task


# @pytest.fixture(scope="session")
@pytest.fixture(scope="session", params=["tiny", "mongo"])
def tasks_db_session(tmpdir_factory, request):
    temp_dir = tmpdir_factory.mktemp("temp")
    tasks.start_tasks_db(str(temp_dir), request.param)
    yield
    tasks.stop_tasks_db()


# @pytest.fixture(scope="session", autouse=True)
@pytest.fixture(scope="session", autouse=True)
def tasks_db(tasks_db_session):
    tasks.delete_all()


@pytest.fixture(scope="session")
def tasks_just_a_few():
    return (
        Task("Write some code", "Brian", True),
        Task("Code review Brian's code", "Katie", False),
        Task("Fix what Brian did", "Michele", False)
    )


@pytest.fixture(scope="session")
def tasks_mult_per_owner():
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),
        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),
        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel')
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_milt_per_owner(tasks_db, tasks_mult_per_owner):
    for t in tasks_mult_per_owner:
        tasks.add(t)


def pytest_report_header():
    return "Thanks for running the tests."


def pytest_report_teststatus(report):
    if report.when == "call" and report.failed:
        return (report.outcome, "0", "OPPORTUNITY for improvement")


def pytest_addoption(parser):
    group = parser.getgroup("nice")
    group.addoption("--nice", action="store_true",
                    help="nice: turn failures into opportunities")
