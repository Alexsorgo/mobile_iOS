import pytest


@pytest.fixture(scope="session")
def pytest_runtest_setup(item):
    """
    Setup test_name_ global pytest variable
    """
    test_name = item.__dict__.get("name").replace("test_", "")
    setattr(item, "test_name_", test_name)
