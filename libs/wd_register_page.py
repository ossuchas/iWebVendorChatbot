# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY


def replyMsg(Reply_token: str = None, line_Acees_Token: str = None):
    authorization = f'Bearer {line_Acees_Token}'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents":
                {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://i.ibb.co/cbYqRfH/register-menu-v1-0.png",
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "gravity": "center",
                                                "aspectRatio": "30:9",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "action",
                                                    "uri": "https://liff.line.me/1653830448-Z2Y9Y3yD"
                                                }
                                            },
                                            {
                                                "type": "separator",
                                                "margin": "sm"
                                            },
                                            {
                                                "type": "image",
                                                "url": "https://i.ibb.co/cLZkC4s/register-menu-v1-0-vendor.png",
                                                "size": "full",
                                                "aspectMode": "cover",
                                                "aspectRatio": "30:9",
                                                "gravity": "center",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "action",
                                                    "uri": "https://liff.line.me/1653830448-j5DnDxlv"
                                                }
                                            }
                                        ],
                                        "flex": 1
                                    }
                                ]
                            }
                        ],
                        "paddingAll": "0px"
                    }
                }
        }

    data = {
        "replyToken": Reply_token,
        "messages": [
            type_msg
        ]
    }

    session = requests.Session()
    response = session.post(LINE_API_REPLY, data=json.dumps(data), headers=headers)
    return 201
