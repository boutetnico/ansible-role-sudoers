[![tests](https://github.com/boutetnico/ansible-role-sudoers/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-sudoers/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.sudoers-blue.svg)](https://galaxy.ansible.com/boutetnico/sudoers)

ansible-role-sudoers
====================

This role configures sudoers.

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

| Variable                | Required | Default              | Choices | Comments                                  |
|-------------------------|----------|----------------------|---------|-------------------------------------------|
| sudoers_dependencies    | yes      |                      | list    | See `defaults/main.yml`.                  |
| sudoers_d_conf          | yes      | `{}`                 | dict    |                                           |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-sudoers
          sudoers_d_conf:
            php-fpm:
              - "envoyer ALL=(ALL) NOPASSWD: /usr/sbin/service php*-fpm reload"

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
