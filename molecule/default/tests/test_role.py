import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file,user,group,mode', [
  ('/tmp/mariadb-java-client-3.0.7.jar', 'root', 'root', 0o644),
])
def test_connector_is_installed(host, file, user, group, mode):
    connector = host.file(file)
    assert connector.exists
    assert connector.is_file
    assert connector.user == user
    assert connector.group == group
    assert connector.mode == mode
