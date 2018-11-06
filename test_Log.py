
'''
test_Log.py: tests to test counts of different log message types from a log file
'''

import sys
import pytest
from logfile import *

# Fixtures
@pytest.fixture
def log(request):
    return Log(request.config.getoption("--inputlog"))

@pytest.mark.parametrize("logtype,expected", [
    ('INFO',50),
    ('WARNING',11),
    ('ERROR',3),
    ('INFO',0),
    ('WARNING',0),
    ('ERROR',0),
    ('INFO',-1),
    ('WARNING',-1),
    ('ERROR',-1),
    ('INFO',9999999999),
    ('WARNING',9999999999),
    ('ERROR',9999999999),
    ('INVALIDLOGTYPE',0),
    ('INVALIDLOGTYPE',-1),
    ('INVALIDLOGTYPE',1),
    (123,123),
    ('',1),
    (None,0),
    (None,1),
    ('INFO',None),
])
def test_LogTypeCount(log,logtype,expected):
    assert expected == log.getCountByType(logtype)
