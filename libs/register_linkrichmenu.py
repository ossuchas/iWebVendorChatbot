# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY
from typing import List
from datetime import datetime

from models.wd_line_chatbot import WDPOStatusModel
from models.poheader import POHeaderModel
from config import CHANNEL_ACCESS_TOKEN, LINE_API_RICHMENU


def linkmenubyuser(user_token_id: str = None, rich_menu: str = None):
    """
    :param user_token_id:
    :param rich_menu:
    :return:
    """

    authorization = f'Bearer {CHANNEL_ACCESS_TOKEN}'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }
    url = f"{LINE_API_RICHMENU}/{user_token_id}/richmenu/{rich_menu}"

    session = requests.Session()
    response = session.post(url=url, headers=headers)
    return 201
