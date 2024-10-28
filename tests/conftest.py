import pytest
import pytest_httpx
import click
import pluggy
import pydantic


@pytest.fixture
def user_path(tmpdir):
    dir = tmpdir / "llm.datasette.io"
    dir.mkdir()
    return dir
