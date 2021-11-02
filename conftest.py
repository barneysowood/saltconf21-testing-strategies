# file: conftest.py
#
# pytest config
#

import pytest

pytest_plugins = [
    "tests.fixtures"
]

def pytest_addoption(parser):
    parser.addoption(
        "--allow-state-apply", action="store_true", default=False, help="run tests that use state.apply and modify state of the system"
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "state_apply: mark test that uses state.apply and modifies state of the system")

def pytest_collection_modifyitems(config, items):
    if config.getoption("--allow-state-apply"):
        # --allow-state-apply given in cli: do not skip state modifying tests
        return
    skip_state_apply = pytest.mark.skip(reason="need --allow-state-apply option to run")
    for item in items:
        if "state_apply" in item.keywords:
            item.add_marker(skip_state_apply)
