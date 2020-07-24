import src.example as example
import pytest
import pytest_check as check

def test_hello_world():
    example.hello_world()
    check.is_true(True)

