from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from flask_cors import CORS
from marshmallow import ValidationError

from db import db
from ma import ma

from resources.chatbot import ChatBot, ChatBotWebhook
from resources.chatbot_register import UserVendorRegister
from resources.userauthen import UserAPRegister

app = Flask(__name__)

api = Api(app, prefix="/api/v1")
CORS(app, resources=r"/api/*", allow_headers="Content-Type")

load_dotenv(".env", verbose=True)
app.config.from_object("config")
app.config.from_envvar("APPLICATION_SETTING")


@app.route('/')
def hello_world():
    return 'AP Line Chat Bot iWeb Vendor v1.0.0'


api.add_resource(ChatBotWebhook, "/webhook")
api.add_resource(UserVendorRegister, "/uservendorregister")
api.add_resource(UserAPRegister, "/userapregister")


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(host="0.0.0.0", port=5000, debug=True)
