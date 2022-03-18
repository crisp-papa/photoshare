from flask import Flask
from app import APP
from flask_login import LoginManager

import debugpy

import app.controllers.db
import app.controllers.route
import app.controllers.user


if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5000)
    # Allow other computers to attach to debugpy at this IP address and port.
    debugpy.listen(('127.0.0.1', 5001))
