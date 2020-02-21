import traceback
from flask_restful import Resource
from flask import request
import json
from datetime import datetime

from libs.register_linkrichmenu import linkmenubyuser
from models.mst_users import UsersModel
from models.chatbot_mst_user import MstUserModel
from config import RICH_MENU_MAIN


class UserVendorRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        try:
            # user_token_id = "U80a30a5bad4ea0f5f7995e5050ab8d7e"
            user_name = user_json["user_name"]
            password = user_json["password"]
            user_token_id = user_json["user_token_id"]
            userObj = UsersModel().check_user_pass(user_name, password)
            # print(user_name, password, user_token_id)
            if not userObj:
                # print("Not Found User")
                return {"message": "Register Failed"}, 401

            # Create Chatbot Master User
            mst_user = MstUserModel()

            mst_user.user_name = user_name
            mst_user.user_token_Id = user_token_id
            mst_user.user_full_name = userObj.FirstName
            mst_user.user_emp_id = userObj.VendorCode
            mst_user.user_status = 'A'
            mst_user.user_empcode = userObj.VendorCode
            mst_user.user_type = 'NOR'
            mst_user.user_position = 'Vendor'
            mst_user.createby = 'APIRegister'
            mst_user.createdate = datetime.now()
            mst_user.modifyby = 'APIRegister'
            mst_user.modifydate = datetime.now()

            mst_user.save_to_db()

            # Link Rich Menu
            rich_menu_link = RICH_MENU_MAIN
            response = linkmenubyuser(user_token_id, rich_menu_link)
            return {"message": "Register Success"}, 200
        except:
            traceback.print_exc()
            return {"message": "Login Failed"}, 500
