from flask_login import login_user

class User(object):
    def __init__(self, incoming):
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False
        self.object_id = incoming['_id']
        self.user_name = incoming['username']

    def get_id(self):
        return str(self.object_id)

    def login_user(self, object_id):
        self.object_id = str(object_id)
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False
        return login_user(self)
