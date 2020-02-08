from models.log_linechatbot import LogChatBotModel
from datetime import datetime


def savechatlog2db(replyToken: str = None,
                   source_groupId: str = None,
                   source_userId: str = None,
                   source_type: str = None,
                   timestamps: str = None,
                   message_type: str = None,
                   message_text: str = None,
                   stickerId: str = None,
                   packageId: str = None,
                   beacon_hwid: str = None,
                   beacon_dm: str = None,
                   beacon_type: str = None,
                   register_flag: str = None,
                   register_empid: str = None,
                   register_email: str = None
                   ) -> int:

    models = LogChatBotModel()

    models.replyToken = replyToken
    models.source_groupId = source_groupId
    models.source_userId = source_userId
    models.source_type = source_type
    models.timestamps = timestamps
    models.message_type = message_type
    models.message_text = message_text
    models.stickerId = stickerId
    models.packageId = packageId
    models.beacon_hwid = beacon_hwid
    models.beacon_dm = beacon_dm
    models.beacon_type = beacon_type
    models.beacon_entrydate = datetime.now()
    models.register_flag = register_flag
    models.register_empid = register_empid
    models.register_email = register_email

    models.save_to_db()

    # products = crm_pd().sp_find_products()

    # print(products[0], products[1])

    return 200