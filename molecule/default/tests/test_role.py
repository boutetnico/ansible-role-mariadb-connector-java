import pytest


@pytest.mark.parametrize(
    "file,user,group,mode",
    [
        ("/tmp/mariadb-java-client-3.4.0.jar", "root", "root", 0o644),
    ],
)
def test_connector_is_installed(host, file, user, group, mode):
    connector = host.file(file)
    assert connector.exists
    assert connector.is_file
    assert connector.user == user
    assert connector.group == group
    assert connector.mode == mode
