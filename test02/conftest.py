import os
import pytest
import yaml


@pytest.fixture(scope="module")
def init_data():
    print("\n开始计算---------------")
    yield
    print("\n结束计算---------------")
