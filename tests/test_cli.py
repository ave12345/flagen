from click.testing import CliRunner

from flagen import build


def test_build():
    """Test build subcommand with default params"""
    runner = CliRunner()
    result = runner.invoke(build)
    assert not result.exception
    assert result.exit_code == 0
    assert 'Done!' in result.output


def test_build_with_template():
    """Test build subcommand with user supplied custom template folder"""
    runner = CliRunner()
    result = runner.invoke(build, ['--template', 'templates/simple'])
    assert not result.exception
    assert result.exit_code == 0
    assert 'Done!' in result.output

    result = runner.invoke(build, ['--template', ''])
    assert result.exception
    assert result.exit_code == 2
    assert 'Invalid value for "--template":' in result.output


def test_build_with_static():
    """Test build subcommand with user supplied static folder"""
    runner = CliRunner()
    result = runner.invoke(build, ['--static', 'static'])
    assert not result.exception
    assert result.exit_code == 0
    assert 'Done!' in result.output

    result = runner.invoke(build, ['--static', ''])
    assert result.exception
    assert result.exit_code == 2
    assert 'Invalid value for "--static":' in result.output


def test_build_all():
    """Test build subcommand with user supplied static and custom template
    folder
    """
    runner = CliRunner()
    result = runner.invoke(
        build, ['--template', 'templates/simple', '--static', 'static'])
    assert not result.exception
    assert result.exit_code == 0
    assert 'Done!' in result.output
