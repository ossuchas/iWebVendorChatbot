# -*- coding: utf-8 -*-

import requests
import json
from config import LINE_API_REPLY
from typing import List
from datetime import datetime

from models.wd_line_chatbot import WDPOStatusModel


def replyMsg(Reply_token: str = None, poObjs: List["WDPOStatusModel"] = None, line_Acees_Token: str = None):
    authorization = 'Bearer {}'.format(line_Acees_Token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': authorization
    }

    print(poObjs)
    new_contents = [
        {"type": "text", "text": "ปริมาณคงเหลือ: 2/5 หน่วย", "color": "#8c8c8c", "size": "xs", "weight": "bold"},
        {"type": "separator", "margin": "sm"},
    ]

    i_count_rec = 0
    for poItem in poObjs:
        # print(poItem.ModifyDateDisplay)
        new_contents.append(
            {"type": "box", "layout": "horizontal",
             "contents": [{"type": "text", "text": "05.02.20 11:46", "size": "sm", "gravity": "center", "flex": 0},
                          {"type": "box", "layout": "vertical", "contents":
                              [{"type": "filler"}, {"type": "box", "layout": "vertical", "contents": [ {"type": "filler"}
                              ], "cornerRadius": "30px", "height": "12px", "width": "12px", "borderColor": "#EF454D", "borderWidth": "2px"}, {"type": "filler"}],
                           "flex": 0 },
                          {"type": "text", "text": "ตั้งหนี้แล้ว", "gravity": "center", "flex": 4, "size": "sm", "color": "#EB3121", "weight": "bold"} ],
             "spacing": "lg", "cornerRadius": "30px", "margin": "md" },  # Set 1
        )
        new_contents.append(
            {"type": "box", "layout": "horizontal", "contents": [{"type": "box", "layout": "baseline", "contents":
                [ {"type": "filler"} ], "flex": 3},{"type": "box", "layout": "vertical", "contents": [ {"type": "box", "layout": "horizontal", "contents": [
                {"type": "filler"}, {"type": "box", "layout": "vertical", "contents": [ {"type": "filler"} ], "width": "2px", "backgroundColor": "#B7B7B7" },
                {"type": "filler"} ], "flex": 1} ], "width": "12px"}, {"type": "text", "text": "38 min", "gravity": "center", "flex": 4, "size": "xs", "color": "#8c8c8c"} ],
             "spacing": "lg", "height": "40px" },  # Set 1
        )
        i_count_rec += 1

    new_contents.append(
        {"type": "separator", "margin": "sm"},
    )
    new_contents.append(
        {"type": "text", "text": "บริษัท ธรรมสรณ์ จำกัด (0000100132)", "size": "xs", "align": "end", "color": "#8c8c8c"},
    )
    print(new_contents)

    type_msg = \
        {
            "type": "flex",
            "altText": "Flex Message",
            "contents":
                {
                    "type": "bubble",
                    "size": "mega",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "เลขที่ใบสั่งซื้อ (PO)", "color": "#fffffff6", "size": "sm" },
                                    { "type": "separator" },
                                    { "type": "text", "text": "4016578316", "color": "#ffffff", "size": "xl", "flex": 4, "weight": "bold" } ]
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
                        #     [
                        #     { "type": "text", "text": "ปริมาณคงเหลือ: 2/5 หน่วย", "color": "#8c8c8c", "size": "xs", "weight": "bold" },
                        #     { "type": "separator", "margin": "sm" },
                        #     { "type": "box", "layout": "horizontal", "contents": [ { "type": "text", "text": "05.02.20 11:46", "size": "sm", "gravity": "center", "flex": 0 },
                        #             { "type": "box", "layout": "vertical", "contents":
                        #                 [ { "type": "filler" }, { "type": "box", "layout": "vertical", "contents": [
                        #                             { "type": "filler" }
                        #                 ], "cornerRadius": "30px", "height": "12px", "width": "12px", "borderColor": "#EF454D", "borderWidth": "2px" },
                        #                     { "type": "filler" } ],
                        #                 "flex": 0
                        #             },
                        #             { "type": "text", "text": "ตั้งหนี้แล้ว", "gravity": "center", "flex": 4, "size": "sm", "color": "#EB3121", "weight": "bold" }
                        #         ],
                        #         "spacing": "lg",
                        #         "cornerRadius": "30px",
                        #         "margin": "md"
                        #     },  # Set 1
                        #     { "type": "box", "layout": "horizontal", "contents": [ { "type": "box", "layout": "baseline", "contents": [
                        #                     { "type": "filler" }
                        #                 ], "flex": 3 },
                        #             { "type": "box", "layout": "vertical", "contents": [ { "type": "box", "layout": "horizontal", "contents": [
                        #                             { "type": "filler" },
                        #                             { "type": "box", "layout": "vertical", "contents": [
                        #                                     { "type": "filler" }
                        #                                 ],
                        #                                 "width": "2px",
                        #                                 "backgroundColor": "#B7B7B7"
                        #                             },
                        #                             { "type": "filler" }
                        #                         ], "flex": 1 }
                        #                 ],
                        #                 "width": "12px"
                        #             },
                        #             { "type": "text", "text": "38 min", "gravity": "center", "flex": 4, "size": "xs", "color": "#8c8c8c" }
                        #         ],
                        #         "spacing": "lg",
                        #         "height": "40px"
                        #     },  # Set 1
                        #     {
                        #         "type": "box",
                        #         "layout": "horizontal",
                        #         "contents": [
                        #             {
                        #                 "type": "text",
                        #                 "text": "05.02.20 11:08",
                        #                 "size": "sm",
                        #                 "gravity": "center",
                        #                 "flex": 0
                        #             },
                        #             {
                        #                 "type": "box",
                        #                 "layout": "vertical",
                        #                 "contents": [
                        #                     {
                        #                         "type": "filler"
                        #                     },
                        #                     {
                        #                         "type": "box",
                        #                         "layout": "vertical",
                        #                         "contents": [
                        #                             {
                        #                                 "type": "filler"
                        #                             }
                        #                         ],
                        #                         "cornerRadius": "30px",
                        #                         "height": "12px",
                        #                         "width": "12px",
                        #                         "borderColor": "#6486E3",
                        #                         "borderWidth": "2px"
                        #                     },
                        #                     {
                        #                         "type": "filler"
                        #                     }
                        #                 ],
                        #                 "flex": 0
                        #             },
                        #             {
                        #                 "type": "text",
                        #                 "text": "อนุมัติวางบิล",
                        #                 "gravity": "center",
                        #                 "flex": 4,
                        #                 "size": "xs",
                        #                 "weight": "bold",
                        #                 "color": "#807671",
                        #                 "wrap": True
                        #             }
                        #         ],
                        #         "spacing": "lg",
                        #         "cornerRadius": "30px",
                        #         "margin": "xs"
                        #     },  # Set 2
                        #     {
                        #         "type": "box",
                        #         "layout": "horizontal",
                        #         "contents": [
                        #             {
                        #                 "type": "box",
                        #                 "layout": "baseline",
                        #                 "contents": [
                        #                     {
                        #                         "type": "filler"
                        #                     }
                        #                 ],
                        #                 "flex": 3
                        #             },
                        #             {
                        #                 "type": "box",
                        #                 "layout": "vertical",
                        #                 "contents": [
                        #                     {
                        #                         "type": "box",
                        #                         "layout": "horizontal",
                        #                         "contents": [
                        #                             {
                        #                                 "type": "filler"
                        #                             },
                        #                             {
                        #                                 "type": "box",
                        #                                 "layout": "vertical",
                        #                                 "contents": [
                        #                                     {
                        #                                         "type": "filler"
                        #                                     }
                        #                                 ],
                        #                                 "width": "2px",
                        #                                 "backgroundColor": "#B7B7B7"
                        #                             },
                        #                             {
                        #                                 "type": "filler"
                        #                             }
                        #                         ],
                        #                         "flex": 1
                        #                     }
                        #                 ],
                        #                 "width": "12px"
                        #             },
                        #             {
                        #                 "type": "text",
                        #                 "text": "5 min",
                        #                 "gravity": "center",
                        #                 "flex": 4,
                        #                 "size": "xs",
                        #                 "color": "#8c8c8c"
                        #             }
                        #         ],
                        #         "spacing": "lg",
                        #         "height": "40px"
                        #     },  # Set 2
                        #     {
                        #         "type": "box",
                        #         "layout": "horizontal",
                        #         "contents": [
                        #             {
                        #                 "type": "text",
                        #                 "text": "05.02.20 11:03",
                        #                 "size": "sm",
                        #                 "gravity": "center",
                        #                 "flex": 0
                        #             },
                        #             {
                        #                 "type": "box",
                        #                 "layout": "vertical",
                        #                 "contents": [
                        #                     {
                        #                         "type": "filler"
                        #                     },
                        #                     {
                        #                         "type": "box",
                        #                         "layout": "vertical",
                        #                         "contents": [
                        #                             {
                        #                                 "type": "filler"
                        #                             }
                        #                         ],
                        #                         "cornerRadius": "30px",
                        #                         "height": "12px",
                        #                         "width": "12px",
                        #                         "borderColor": "#6486E3",
                        #                         "borderWidth": "2px"
                        #                     },
                        #                     {
                        #                         "type": "filler"
                        #                     }
                        #                 ],
                        #                 "flex": 0
                        #             },
                        #             {
                        #                 "type": "text",
                        #                 "text": "รอตรวจเอกสารวางบิล",
                        #                 "gravity": "center",
                        #                 "flex": 4,
                        #                 "size": "xs",
                        #                 "weight": "bold",
                        #                 "color": "#807671",
                        #                 "wrap": True
                        #             }
                        #         ],
                        #         "spacing": "lg",
                        #         "cornerRadius": "30px",
                        #         "margin": "xs"
                        #     },
                        #     {
                        #         "type": "box",
                        #         "layout": "horizontal",
                        #         "contents": [
                        #             {
                        #                 "type": "box",
                        #                 "layout": "baseline",
                        #                 "contents": [
                        #                     {
                        #                         "type": "filler"
                        #                     }
                        #                 ],
                        #                 "flex": 3
                        #             },
                        #             {
                        #                 "type": "box",
                        #                 "layout": "vertical",
                        #                 "contents": [
                        #                     {
                        #                         "type": "box",
                        #                         "layout": "horizontal",
                        #                         "contents": [
                        #                             {
                        #                                 "type": "filler"
                        #                             },
                        #                             {
                        #                                 "type": "box",
                        #                                 "layout": "vertical",
                        #                                 "contents": [
                        #                                     {
                        #                                         "type": "filler"
                        #                                     }
                        #                                 ],
                        #                                 "width": "2px",
                        #                                 "backgroundColor": "#B7B7B7"
                        #                             },
                        #                             {
                        #                                 "type": "filler"
                        #                             }
                        #                         ],
                        #                         "flex": 1
                        #                     }
                        #                 ],
                        #                 "width": "12px"
                        #             },
                        #             {
                        #                 "type": "text",
                        #                 "text": "24H32mins",
                        #                 "gravity": "center",
                        #                 "flex": 4,
                        #                 "size": "xs",
                        #                 "color": "#8c8c8c"
                        #             }
                        #         ],
                        #         "spacing": "lg",
                        #         "height": "40px"
                        #     },
                        #     {
                        #         "type": "box",
                        #         "layout": "horizontal",
                        #         "contents": [
                        #             {
                        #                 "type": "text",
                        #                 "text": "04.02.20 11:39",
                        #                 "size": "sm",
                        #                 "gravity": "center",
                        #                 "flex": 0
                        #             },
                        #             {
                        #                 "type": "box",
                        #                 "layout": "vertical",
                        #                 "contents": [
                        #                     {
                        #                         "type": "filler"
                        #                     },
                        #                     {
                        #                         "type": "box",
                        #                         "layout": "vertical",
                        #                         "contents": [
                        #                             {
                        #                                 "type": "filler"
                        #                             }
                        #                         ],
                        #                         "cornerRadius": "30px",
                        #                         "height": "12px",
                        #                         "width": "12px",
                        #                         "borderColor": "#6486E3",
                        #                         "borderWidth": "2px"
                        #                     },
                        #                     {
                        #                         "type": "filler"
                        #                     }
                        #                 ],
                        #                 "flex": 0
                        #             },
                        #             {
                        #                 "type": "text",
                        #                 "text": "รอการวางบิล (ทำ GR แล้ว)",
                        #                 "gravity": "center",
                        #                 "flex": 4,
                        #                 "size": "xs",
                        #                 "weight": "bold",
                        #                 "color": "#807671",
                        #                 "wrap": True
                        #             }
                        #         ],
                        #         "spacing": "lg",
                        #         "cornerRadius": "30px",
                        #         "margin": "xs"
                        #     },
                        #     {
                        #         "type": "box",
                        #         "layout": "horizontal",
                        #         "contents": [
                        #             {
                        #                 "type": "box",
                        #                 "layout": "baseline",
                        #                 "contents": [
                        #                     {
                        #                         "type": "filler"
                        #                     }
                        #                 ],
                        #                 "flex": 3
                        #             },
                        #             {
                        #                 "type": "box",
                        #                 "layout": "vertical",
                        #                 "contents": [
                        #                     {
                        #                         "type": "box",
                        #                         "layout": "horizontal",
                        #                         "contents": [
                        #                             {
                        #                                 "type": "filler"
                        #                             },
                        #                             {
                        #                                 "type": "box",
                        #                                 "layout": "vertical",
                        #                                 "contents": [
                        #                                     {
                        #                                         "type": "filler"
                        #                                     }
                        #                                 ],
                        #                                 "width": "2px",
                        #                                 "backgroundColor": "#B7B7B7"
                        #                             },
                        #                             {
                        #                                 "type": "filler"
                        #                             }
                        #                         ],
                        #                         "flex": 1
                        #                     }
                        #                 ],
                        #                 "width": "12px"
                        #             },
                        #             {
                        #                 "type": "text",
                        #                 "text": "55 min",
                        #                 "gravity": "center",
                        #                 "flex": 4,
                        #                 "size": "xs",
                        #                 "color": "#8c8c8c"
                        #             }
                        #         ],
                        #         "spacing": "lg",
                        #         "height": "40px"
                        #     },
                        #     {
                        #         "type": "box",
                        #         "layout": "horizontal",
                        #         "contents": [
                        #             {
                        #                 "type": "text",
                        #                 "text": "04.02.20 10:46",
                        #                 "size": "sm",
                        #                 "gravity": "center",
                        #                 "flex": 0
                        #             },
                        #             {
                        #                 "type": "box",
                        #                 "layout": "vertical",
                        #                 "contents": [
                        #                     {
                        #                         "type": "filler"
                        #                     },
                        #                     {
                        #                         "type": "box",
                        #                         "layout": "vertical",
                        #                         "contents": [
                        #                             {
                        #                                 "type": "filler"
                        #                             }
                        #                         ],
                        #                         "cornerRadius": "30px",
                        #                         "height": "12px",
                        #                         "width": "12px",
                        #                         "borderColor": "#6486E3",
                        #                         "borderWidth": "2px"
                        #                     },
                        #                     {
                        #                         "type": "filler"
                        #                     }
                        #                 ],
                        #                 "flex": 0
                        #             },
                        #             {
                        #                 "type": "text",
                        #                 "text": "อนุมัติรับสินค้า (รอทำ GR)",
                        #                 "gravity": "center",
                        #                 "flex": 4,
                        #                 "size": "xs",
                        #                 "weight": "bold",
                        #                 "color": "#807671",
                        #                 "wrap": True
                        #             }
                        #         ],
                        #         "spacing": "lg",
                        #         "cornerRadius": "30px",
                        #         "margin": "xs"
                        #     },
                        #     { "type": "separator", "margin": "sm" },
                        #     { "type": "text", "text": "บริษัท ธรรมสรณ์ จำกัด (0000100132)", "size": "xs", "align": "end", "color": "#8c8c8c" }
                        # ]
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
