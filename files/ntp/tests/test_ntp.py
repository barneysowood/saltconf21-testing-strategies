import pytest

def test_state_show_sls(salt_caller):
    result = salt_caller.test_state_show_sls('ntp')
    assert result

def test_state_apply_mock(salt_caller):
    result = salt_caller.test_state_apply('ntp', mock=True)
    assert result

@pytest.mark.state_apply
def test_state_apply(salt_caller, host):
    result = salt_caller.test_state_apply('ntp')
    assert result
    assert host.package("ntp").is_installed

    ntp_conf = host.file("/etc/ntp.conf")
    assert ntp_conf.exists
    assert ntp_conf.user == "root"
    assert ntp_conf.group == "root"
    assert ntp_conf.mode == 0o640

    assert host.service('ntp').is_running
    assert host.service('ntp').is_enabled