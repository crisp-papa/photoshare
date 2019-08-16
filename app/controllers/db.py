from pymongo import MongoClient
from bson.objectid import ObjectId

import logging
import sys

class PhotoshareDatabase(object):
    def __init__(self):
        try:
            self.client = MongoClient('localhost', 27017)
            self.db = self.client
        except Exception:
            # Log exception
            logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
            logging.debug('Something not right happened')

    def create_user(self, user):
        result = self.client.photoshare.users.insert_one(user)
        if result:
            return result.inserted_id

        return None

    def get_user(self, user):
        result = self.client.photoshare.users.find_one({
            'username': user['username'],
            'password': user['password']
        })

        if result:
            return result._id
        
        return 'User not found'

    def get_user_by_name(self, username):
        user = self.client.photoshare.users.find_one({'username': username})

        if user:
            return user
        
        return 'User not found'

    def get_user_by_id(self, user_id):
        user = self.client.photoshare.users.find_one(ObjectId(user_id), projection={'_id': False})
        
        if user:
            return user

        return 'User not found'

    def get_access(self, access_code):
        verify = self.client.photoshare.codes.find_one({ 'access_code': access_code })

        if (verify):
            return True

        return False
    