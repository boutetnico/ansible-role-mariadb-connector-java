[![tests](https://github.com/boutetnico/ansible-role-mariadb-connector-java/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-mariadb-connector-java/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.mariadb_connector_java-blue.svg)](https://galaxy.ansible.com/boutetnico/mariadb_connector_java)

ansible-role-mariadb-connector-java
===================================

This role installs [MariaDB Connector/J](https://mariadb.com/kb/en/about-mariadb-connector-j/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                     | Required | Default             | Choices   | Comments                                      |
|------------------------------|----------|---------------------|-----------|-----------------------------------------------|
| connector_dependencies       | yes      | `[]`                | list      |                                               |
| connector_version            | yes      | `3.5.7`             | string    |                                               |
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
