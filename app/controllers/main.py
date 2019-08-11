from app import APP
from flask import render_template, flash, request, redirect, url_for
import bcrypt
from app.controllers.db import PhotoshareDatabase

@APP.route('/', methods=['GET'])
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


# def get_hashed_password(plain_text_password):
#     # Hash a password for the first time
#     #   (Using bcrypt, the salt is saved into the hash itself)
#     return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

# def check_password(plain_text_password, hashed_password):
#     # Check hashed password. Using bcrypt, the salt is saved into the hash itself
#     return bcrypt.checkpw(plain_text_password, hashed_password)