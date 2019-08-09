from flask import Flask
from app import APP
import app.controllers.main

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=6999)
    
    