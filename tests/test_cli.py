from click.testing import CliRunner

from template import cli


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(cli, [])
    assert result.exit_code == 0
    assert result.output == "Hello world!\n"
