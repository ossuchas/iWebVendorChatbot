import traceback
from flask_restful import Resource
from flask import request
import re

from datetime import datetime, timedelta

from libs import chatbot_helper, log_linechatbot as logs, \
    wd_check_status, wd_all_status, check_po, wd_register_page


from config import CHANNEL_ACCESS_TOKEN, REPLY_WORDING, \
    DEFAULT_REPLY_WORDING, ERROR_NUMB_ONLY, MENU_01_CHECK_PO, \
    ERROR_NUMB_LEN, ERROR_NUMB_PREFIX_PO, FIND_PO_TRAN_ID, \
    UNDER_CONSTRUCTION, ERROR_PO_NOT_EXISTING, ERROR_PO_NOT_FOUND, \
    MSG_REGISTER, REGISTER_MSG


from models.chatbot_mst_user import MstUserModel
from models.wd_line_chatbot import WDPOStatusModel
from models.wd_all_line_chatbot import WDPOAllStatusModel
from models.poheader import POHeaderModel


class ChatBot(Resource):
    @classmethod
    def get(cls):
        return {"message": "Hello World"}, 200


class ChatBotWebhook(Resource):
    @classmethod
    def post(cls):
        payload = request.get_json()
        print(payload)

        reply_token = payload['events'][0]['replyToken']
        source_type = payload['events'][0]['source']['type']
        timestamps = payload['events'][0]['timestamp']

        # get event type beacon or message
        events_type = payload['events'][0]['type']
        # print(events_type)

        groupId = None
        userId = None
        stickerId = None
        packageId = None
        msg_text = None
        name = None
        beacon_hwid = None
        beacon_dm = None
        beacon_type = None

        # Register Flag
        register_flag = 'N'
        register_empid = None
        register_email = None

        try:
            groupId = payload['events'][0]['source']['groupId']
            userId = payload['events'][0]['source']['userId']
            # print(userId, groupId)
        except:
            userId = payload['events'][0]['source']['userId']

        if events_type == 'message':
            msg_type = payload['events'][0]['message']['type']
        elif events_type == 'postback':
            msg_type = 'postback'
        else:
            msg_type = 'beacon'

        reply_msg = None

        if msg_type == 'text':
            msg_text = payload['events'][0]['message']['text']
            message = msg_text
            # print(userId)
            user = MstUserModel().check_auth_by_token_id(userId)

            if user:
                if message == MENU_01_CHECK_PO:  # Push Menu 01
                    pass
                elif re.match(REGISTER_MSG, message):  # After Register
                    pass
                elif re.match(FIND_PO_TRAN_ID, message):  # trans_id=xxxx
                    values = message.split("=")
                    tran_id = values[1]
                    poObjs = WDPOStatusModel().find_by_tran_id(tran_id)
                    # print(poObjs)
                    wd_check_status.replyMsg(reply_token, poObjs, CHANNEL_ACCESS_TOKEN)
                elif message.isdigit():
                    if len(message) != 10:
                        # print("Len Not Equal 10")
                        reply_msg = ERROR_NUMB_LEN
                        chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                    elif message[0:2] != '40':
                        # print("Not Equal Prefix 40")
                        reply_msg = ERROR_NUMB_PREFIX_PO
                        chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
                    else:
                        # print("find PO Status")
                        if user.user_type == 'VIP':
                            poObjs = WDPOAllStatusModel().find_by_po(message)
                            if not poObjs:
                                reply_msg = ERROR_PO_NOT_FOUND
                                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)

                            wd_all_status.replyMsg(reply_token, poObjs, CHANNEL_ACCESS_TOKEN)
                        else:
                            # print("by Vendor Name")
                            po_existing = POHeaderModel().find_by_poid_by_vendor(_po_id=message,
                                                                                 _vendor_id=user.user_name)
                            if not po_existing:
                                reply_msg = ERROR_PO_NOT_EXISTING
                                chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)

                            poObjs = WDPOAllStatusModel().find_by_po(message)
                            wd_all_status.replyMsg(reply_token, poObjs, CHANNEL_ACCESS_TOKEN)
                elif re.match(UNDER_CONSTRUCTION, message):
                    # print("under construction")
                    pass
                else:
                    # print("is Not Number")
                    reply_msg = ERROR_NUMB_ONLY
                    chatbot_helper.replyMsg(reply_token, reply_msg, CHANNEL_ACCESS_TOKEN)
            else:  # Register
                if re.match(REGISTER_MSG, message):  # After Register
                    pass
                else:
                    print('user not found')
                    wd_register_page.replyMsg(reply_token, CHANNEL_ACCESS_TOKEN)
                # print("not found")
        elif msg_type == 'image':  # Image Upload to Line Bot
            image_id = payload['events'][0]['message']['id']
            contentProvider = payload['events'][0]['message']['contentProvider']['type']
            print(f"{image_id} , {contentProvider}")
        elif msg_type == 'location':
            location_id = payload['events'][0]['message']['id']
            address = payload['events'][0]['message']['address']
            latitude = payload['events'][0]['message']['latitude']
            longitude = payload['events'][0]['message']['longitude']
            pass
        elif msg_type == 'postback':
            param_data = payload['events'][0]['postback']['data']
            print(param_data)
            richmenuId = None
            # if param_data == 'next':
            #     richmenuId = RICH_MENU_SECOND
            # elif param_data == 'back':
            #     richmenuId = RICH_MENU_MAIN
            # else:
            #     pass
            # chatbot_rich_menu.replyMsg(userId=userId,
            #                            richMenuId=richmenuId,
            #                            line_aceess_token=CHANNEL_ACCESS_TOKEN)
        elif msg_type == 'beacon':
            beacon_hwid = payload['events'][0]['beacon']['hwid']
            beacon_dm = payload['events'][0]['beacon']['dm']
            beacon_type = payload['events'][0]['beacon']['type']
            stickerId = None
            packageId = None
            msg_text = None

            user = MstUserModel().find_by_token_id(userId)
        else:
            if msg_type == 'sticker':
                stickerId = payload['events'][0]['message']['stickerId']
                packageId = payload['events'][0]['message']['packageId']
            else:
                stickerId = None
                packageId = None
                msg_text = None

        # Save Log to DB
        logs.savechatlog2db(reply_token, groupId,
                            userId, source_type,
                            timestamps, msg_type,
                            msg_text, stickerId, packageId,
                            beacon_hwid, beacon_dm, beacon_type,
                            register_flag, register_empid, register_email)

        return {"message": "Register Line Push and Reply Message Successful"}, 201
