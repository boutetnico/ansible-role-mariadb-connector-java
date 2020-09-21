ansible-role-mariadb-connector-java
===================================

This role installs [MariaDB Connector/J](https://mariadb.com/kb/en/about-mariadb-connector-j/).

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                     | Required | Default             | Choices   | Comments                                      |
|------------------------------|----------|---------------------|-----------|-----------------------------------------------|
| connector_dependencies       | yes      | `[]`                | list      |                                               |
| connector_version            | yes      | `2.6.2`             | string    |                                               |
| connector_install_path       | yes      | `/tmp`              | string    |                                               |
| connector_owner              | yes      | `root`              | string    |                                               |
| connector_group              | yes      | `root`              | string    |                                               |
| connector_mode               | yes      | `0644`              | string    |                                               |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-mariadb-connector-java

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
