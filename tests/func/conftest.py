import pytest

from src import tasks


@pytest.fixture(autouse=True)
def initialise_tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), "tiny")
    yield
    tasks.stop_tasks_db()
