from ma import ma
from models.wd_line_chatbot import WDPOStatusModel


class WDPOStatusSchema(ma.ModelSchema):
    class Meta:
        model = WDPOStatusModel
