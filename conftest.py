import pytest

def pytest_addoption(parser):
    parser.addoption("--inputlog", action="store", default="test.log")
