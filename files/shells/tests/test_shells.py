import pytest

def test_state_show_sls(salt_caller):
    result = salt_caller.test_state_show_sls('shells')
    assert result

def test_state_apply_mock(salt_caller):
    result = salt_caller.test_state_apply('shells', mock=True)
    assert result

@pytest.mark.state_apply
def test_state_apply(salt_caller, host):
    result = salt_caller.test_state_apply('shells')
    assert result
    assert host.file("/etc/shells").contains("#/bin/dash")
