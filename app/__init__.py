from flask import Flask
from settings import Config
from app.registers import registerApp, registerLib


def createApp():
    app = Flask(__name__)
    app.config.from_object(Config)

    registerApp(app)
    registerLib(app)

    return app


app = createApp()
