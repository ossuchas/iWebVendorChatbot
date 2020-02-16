# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY
from typing import List
from datetime import datetime

from models.wd_all_line_chatbot import WDPOAllStatusModel
from models.poheader import POHeaderModel


def replyMsg(Reply_token: str = None, poObjs: List["WDPOAllStatusModel"] = None, line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    # print(poObjs)
    new_contents = [
            { "type": "separator", "margin": "sm" },
            { "type": "box", "layout": "baseline", "contents": [ { "type": "text", "text": "วันที่ส่งงาน", "size": "sm", "weight": "bold" },
                    { "type": "text", "text": "สถานะล่าสุด", "size": "sm", "align": "end", "weight": "bold" },
                    { "type": "text", "text": "ดูรายละเอียด", "align": "end", "size": "sm", "weight": "bold" }
                ],
                "backgroundColor": "#00FF9F"
            },
    ]

    i_count_rec = 0
    poid_display = None
    for poItem in poObjs:
        # print(poItem.ModifyDateDisplay)
        if i_count_rec % 2 == 0:
            bg_color_row = "#FFFFFF"
        else:
            # bg_color_row = "#EBEDEF"
            bg_color_row = "#FAF5FF"

        action = f"tran_id={poItem.tran_id}"
        poid_display = poItem.poid

        new_contents.append(
            {"type": "box", "layout": "horizontal",
             "contents": [{"type": "text", "text": poItem.CreateDateDisplay, "size": "sm", "gravity": "center"},
                          {"type": "text", "text": poItem.Doc_Status, "size": "sm", "wrap": True, "align": "end", "gravity": "center"},
                          {"type": "image", "url": "https://i.ibb.co/nkJRv9n/search.png",
                           "action": {"type": "message", "label": "action", "text": action}, "size": "sm",
                           "aspectMode": "fit", "aspectRatio": "27:14", "align": "end"}
                          ],
             "backgroundColor": bg_color_row,
             "margin": "sm"
             },
        )
        i_count_rec += 1

    poH = POHeaderModel().find_by_poid(poid_display)
    print(poH)
    vendor_display = f"{poH.vendorname} ({poH.vendorid})"
    new_contents.append(
        {"type": "separator", "margin": "sm"},
    )
    new_contents.append(
        {"type": "text", "text": vendor_display, "size": "xs", "align": "end", "color": "#8c8c8c"},
    )
    print(new_contents)

    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents":
                {
                    "type": "bubble",
                    "size": "giga",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "เลขที่ใบสั่งซื้อ (PO)",
                                        "color": "#fffffff6",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "separator"
                                    },
                                    {
                                        "type": "text",
                                        "text": poid_display,
                                        "color": "#ffffff",
                                        "size": "xl",
                                        "flex": 4,
                                        "weight": "bold"
                                    }
                                ]
                            }
                        ],
                        "paddingAll": "20px",
                        "backgroundColor": "#0367D3",
                        "spacing": "md",
                        "height": "80px",
                        "paddingTop": "22px"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": new_contents
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Copyright 2020 AP (Thailand) PCL.",
                                "align": "center",
                                "size": "xs",
                                "color": "#FFFFFF"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://i.ibb.co/fS0B4wP/AP-Logo-2018.png"
                                    }
                                ],
                                "position": "absolute",
                                "height": "30px",
                                "width": "32px",
                                "offsetBottom": "3px"
                            }
                        ],
                        "backgroundColor": "#000000"
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
