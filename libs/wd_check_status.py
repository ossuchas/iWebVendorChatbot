# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY
from typing import List
from datetime import datetime

from models.wd_line_chatbot import WDPOStatusModel
from models.poheader import POHeaderModel


def replyMsg(Reply_token: str = None, poObjs: List["WDPOStatusModel"] = None, line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    # print(poObjs)
    new_contents = [
        # {"type": "text", "text": "ปริมาณคงเหลือ: 2/5 หน่วย", "color": "#8c8c8c", "size": "xs", "weight": "bold"},
        {"type": "separator", "margin": "sm"},
    ]

    Date_before = datetime.now()
    i_count_rec = 0
    duration_list = []
    for poItem in poObjs:
        duration = Date_before - poItem.ModifyDate
        duration_in_s = duration.total_seconds()
        days = divmod(duration_in_s, 86400)
        hours = divmod(days[1], 3600)
        minutes = divmod(hours[1], 60)
        time2display = f"{days[0]:,.0f}d{hours[0]:,.0f}h{minutes[0]:,.0f}m"
        if i_count_rec > 0:
            duration_list.append(time2display)
        # print(Date_before, poItem.ModifyDate, duration, duration_in_s, days[0], hours[0], minutes[0], time2display)

        Date_before = poItem.ModifyDate
        i_count_rec += 1

    duration_list.append("-")
    # print(duration_list)

    i_count_rec = 0
    poid_display = None
    poid = None
    for poItem in poObjs:
        if i_count_rec != 0:
            point_color = "#6486E3"
        else:
            point_color = "#ed3939"
        new_contents.append(
            {"type": "box", "layout": "horizontal",
             "contents": [{"type": "text", "text": poItem.ModifyDateDisplay, "size": "sm", "gravity": "center", "flex": 0},
                          {"type": "box", "layout": "vertical", "contents":
                              [{"type": "filler"}, {"type": "box", "layout": "vertical", "contents": [ {"type": "filler"}
                              ], "cornerRadius": "30px", "height": "12px", "width": "12px", "borderColor": point_color, "borderWidth": "2px"}, {"type": "filler"}],
                           "flex": 0 },
                          {"type": "text", "text": poItem.Doc_Status, "gravity": "center", "flex": 4, "size": "sm", "color": "#807671", "weight": "bold"} ],
             "spacing": "lg", "cornerRadius": "30px", "margin": "md" },  # Set 1
        )
        new_contents.append(
            {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "baseline", "contents":
                [ {"type": "filler"} ], "flex": 3},{"type": "box", "layout": "vertical", "contents": [ {"type": "box", "layout": "horizontal", "contents": [
                {"type": "filler"}, {"type": "box", "layout": "vertical", "contents": [ {"type": "filler"} ], "width": "2px", "backgroundColor": "#B7B7B7" },
                {"type": "filler"} ], "flex": 1} ], "width": "12px"}, {"type": "text", "text": duration_list[i_count_rec], "gravity": "center", "flex": 4, "size": "xs", "color": "#8c8c8c"} ],
             "spacing": "lg", "height": "40px", "width": "260px" },  # Set 1
        )
        poid_display = f"{poItem.POID} [{poItem.Tran_Id}]"
        poid = f"{poItem.POID}"

        # Diff Date
        # duration = poItem.ModifyDate - Date_before

        i_count_rec += 1

    poH = POHeaderModel().find_by_poid(poid)
    print(poH, poid, i_count_rec)
    vendor_display = f"{poH.vendorname} ({poH.vendorid})"

    new_contents.append(
        {"type": "separator", "margin": "sm"},
    )
    new_contents.append(
        {"type": "text", "text": vendor_display, "size": "xs", "align": "end", "color": "#8c8c8c"},
    )
    # print(new_contents)

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
                            { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "เลขที่ใบสั่งซื้อ (PO)", "color": "#fffffff6", "size": "sm" },
                                    { "type": "separator" },
                                    { "type": "text", "text": poid_display, "color": "#ffffff", "size": "xl", "flex": 4, "weight": "bold" } ]
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
                        "contents":  new_contents
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
