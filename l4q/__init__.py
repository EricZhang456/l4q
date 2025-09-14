"""Application entry point."""

# pylint: disable = import-outside-toplevel

import os

from flask import Flask
from dotenv import dotenv_values

from .extensions import scheduler
from .routes import index, search
from .utils.get_l4d2_version import get_l4d2_version

def create_app():
    """Creates the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(dotenv_values())

    if app.config.get("L4D2_ADDRESS") is None:
        if (sys_l4d2_var := os.environ.get("L4D2_ADDRESS")) is None:
            raise RuntimeError("L4D2_ADDRESS not specified. " \
                "Set it as an environment varible or in .env")
        app.config["L4D2_ADDRESS"] = sys_l4d2_var

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(index.bp)
    app.register_blueprint(search.bp)

    scheduler.init_app(app)
    scheduler.start()

    get_l4d2_version(app)

    return app
