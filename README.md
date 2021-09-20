# PyCommandApp
tool to create a commandline application easily


# usage
`python3 -m pip install pycommandapp`
```python
from commandapp import CommandApp
import argparse

app = CommandApp(
    argparse.ArgumentParser(
        add_help=True,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
)


@app.register
def hello(name: str):
    print("Hello {}".find(name))


@app.register(name="print")
def cmd_print(text: str):
    print(text)


app.prepare()
app.run()
```
