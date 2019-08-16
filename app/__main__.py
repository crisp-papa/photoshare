from flask import Flask
from app import APP
from flask_login import LoginManager

import app.controllers.db
import app.controllers.route
import app.controllers.user


if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=6999)
