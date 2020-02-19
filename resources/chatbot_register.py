import traceback
from flask_restful import Resource
from flask import request
import json

from libs.register_linkrichmenu import linkmenubyuser
from config import RICH_MENU_MAIN


class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        try:
            # user_token_id = "U80a30a5bad4ea0f5f7995e5050ab8d7e"
            user_token_id = user_json["user_token_id"]
            rich_menu_link = RICH_MENU_MAIN
            response = linkmenubyuser(user_token_id, rich_menu_link)
            return {"message": "Register Successful"}, 200
            # return json.loads(response.content), 200
        except:
            traceback.print_exc()
            return {"message": "Login Failed"}, 500
