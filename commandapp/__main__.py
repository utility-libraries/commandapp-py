import commandapp as cmdapp


app = cmdapp.CommandApp()

app.version = cmdapp.__version__

app.run()
