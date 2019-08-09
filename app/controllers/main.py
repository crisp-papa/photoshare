from app import APP
from flask import render_template, flash

@APP.route('/', methods=['GET'])
def invite():
    # flash('very interesting')
    return render_template('invite.html')
