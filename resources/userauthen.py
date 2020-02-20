import traceback
from flask_restful import Resource
from flask import request
import json

from libs.ap_authen import APAuthen, APAuthenException


class UserAPRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        try:
            user_token_id = user_json["user_token_id"]
            print(user_token_id)
            response = APAuthen.ap_authen(user_json["user_name"], user_json["password"], "APINTRANET")
            return {"message": "Successful Authentication"}, 200
            # return json.loads(response.content), 200
        except APAuthenException as e:
            return {"message": str(e)}, 401
        except:
            traceback.print_exc()
            return {"message": "Login Failed"}, 500
