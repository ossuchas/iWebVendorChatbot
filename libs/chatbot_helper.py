import os
import re
import requests
import json
from config import LINE_API_REPLY


def replyMsg(reply_token, text_msg, line_aceess_token):

    authorization = f"Bearer {line_aceess_token}"
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    type_msg = {
        "type": "text",
        "text": text_msg
    }

    data = {
        "replyToken": reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API_REPLY, data=json.dumps(data), headers=headers)
    return 201
