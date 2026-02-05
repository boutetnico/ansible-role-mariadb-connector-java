import pytest


@pytest.mark.parametrize(
    "file,user,group,mode",
    [
        ("/tmp/mariadb-java-client-3.5.7.jar", "root", "root", 0o644),
    ],
)
def test_connector_is_installed(host, file, user, group, mode):
    connector = host.file(file)
    assert connector.exists
    assert connector.is_file
    assert connector.user == user
    assert connector.group == group
    assert connector.mode == mode


def test_connector_jar_is_valid(host):
    """Test that the JAR file is a valid Java archive."""
    cmd = host.run(
        "python3 -c \"import zipfile; print(zipfile.is_zipfile('/tmp/mariadb-java-client-3.5.7.jar'))\""
    )
    assert cmd.rc == 0
    assert "True" in cmd.stdout
