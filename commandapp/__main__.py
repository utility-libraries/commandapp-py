import sys
import shlex
if len(sys.argv) <= 1:
    sys.argv.extend(shlex.split(input("=> ")))
import commandapp as cmdapp
import typing as t


app = cmdapp.CommandApp()

app.version = cmdapp.__version__


@app.register
def test(param: t.Union[int, str], other: int):
    r"""
    simple test command
    """
    print("Test success")
    print([param, other])


def subcmd():
    raise RuntimeError()


@app.register(name='raise')
def cmd_raise():
    r"""
    command to test exception output
    """
    subcmd()


app.run()
