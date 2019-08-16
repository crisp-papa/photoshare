import bcrypt

from app import APP
from app.controllers.db import PhotoshareDatabase
from app.controllers.user import User

from flask import render_template, flash, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

login_manager = LoginManager()
login_manager.init_app(APP)
login_manager.login_view = 'login'
users = {}

@APP.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@APP.route('/invite', methods=['GET', 'POST'])
def invite():
    psdb = PhotoshareDatabase()
    code = request.args.get('code')
    if (code and psdb.get_access(code)):
        flash(f"Your access code is: {request.args.get('code')}", 'message')
    else:
        # Boot em back home and flash message to go away
        flash('Wrong code', 'error')
        return redirect(url_for('index'))

    if (request.method == 'POST'):
        user = request.form.to_dict()

        # Backend validation on passwords matching
        if (user['password'] == user['password-confirm']):
            # salt and hash password and then insert into db
            tastyHash = bcrypt.hashpw(user['password'], bcrypt.gensalt(7))
            postUser = {
                'username': user['username'],
                'password': tastyHash
            }

            psdb.create_user(postUser)
            
    return render_template('invite.html')

@APP.route('/login', methods=['GET', 'POST'])
def login():
    psdb = PhotoshareDatabase()

    if (request.method == 'POST'):
        user = request.form.to_dict()
        db_user = psdb.get_user_by_name(user['username'])

        if (bcrypt.checkpw(user['password'], db_user['password'])):
            user = User(db_user)
            login_user(user)
            users[user.get_id()] = user

            flash('Welcome back!', 'success')

        else:
            flash('Password incorrect, please try again', 'error')

        return redirect(url_for('index'))

    return render_template('login.html')

@login_manager.user_loader
def load_user(user_id):
    try:
        ret = users[user_id]
    except Exception:
        return None
    return users[user_id]

@APP.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))