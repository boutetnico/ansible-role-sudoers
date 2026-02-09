import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("sudo"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "file,user,group,mode,line",
    [
        (
            "/etc/sudoers.d/php-fpm",
            "root",
            "root",
            "0440",
            "envoyer ALL=(ALL) NOPASSWD: /usr/sbin/service php*-fpm reload",
        ),
        (
            "/etc/sudoers.d/nginx",
            "root",
            "root",
            "0440",
            "deploy ALL=(ALL) NOPASSWD: /usr/sbin/service nginx reload",
        ),
    ],
)
def test_sudoers_file(host, file, user, group, mode, line):
    f = host.file(file)
    assert f.exists
    assert f.is_file
    assert f.user == user
    assert f.group == group
    assert f.mode == int(mode, 8)
    assert line in f.content_string


def test_nginx_sudoers_has_multiple_lines(host):
    f = host.file("/etc/sudoers.d/nginx")
    assert (
        "deploy ALL=(ALL) NOPASSWD: /usr/sbin/service nginx reload" in f.content_string
    )
    assert (
        "deploy ALL=(ALL) NOPASSWD: /usr/sbin/service nginx restart" in f.content_string
    )
