from app import APP
from flask import render_template, flash

@APP.route('/', methods=['GET'])
def invite():
    flash('success!', 'success')
    flash('error', 'error')
    flash('warning!?', 'warning')
    flash('just a message', 'message')
    return render_template('shared/main.html')
