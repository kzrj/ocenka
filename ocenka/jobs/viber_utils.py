# # -*- coding: utf-8 -*-
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages import (
        TextMessage,
        ContactMessage,
        PictureMessage,
        VideoMessage,
        URLMessage,
        KeyboardMessage
    )
from viberbot.api.messages.data_types.contact import Contact

from viberbot.api.viber_requests import (
    ViberConversationStartedRequest,
    ViberFailedRequest,
    ViberMessageRequest,
    ViberSubscribedRequest,
    ViberUnsubscribedRequest,
    ViberDeliveredRequest,
    ViberSeenRequest
    )

viber = Api(BotConfiguration(
    name='dm-eda',
    avatar='http://site.com/avatar.jpg',
    auth_token='4ba8b47627e7dd45-896232bcd5f44988-d6eba79009c0e27'
))


def login_keyboard(viber_id=None):
    # get or create user with profile.viber_id = viber_id
    # gen token
    token = 'token'
    return {
            "Type": "keyboard",
            "Buttons": [
               {
                    "Columns": 1,
                    "Rows": 2,
                    "Text": "<br><font color=#494E67><b>Открыть сайт</b></font>",
                    "TextSize": "regular",
                    "TextHAlign": "center",
                    "TextVAlign": "middle",
                    "ActionType": "open-url",
                    "ActionBody": f"https://svoyaeda.su/dm/login/v/{viber_id}",
                    "OpenURLType": "internal",
                    "BgColor": "#f7bb3f",
                    "Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
                },
                {
                    "Columns": 1,
                    "Rows": 2,
                    "BgColor": "#e6f5ff",
                    "BgMedia": "http://link.to.button.image",
                    "BgMediaType": "picture",
                    "BgLoop": True,
                    "ActionType": "reply",
                    "ActionBody": "MASS_MESSAGES",
                    "ReplyType": "message",
                    "Text": "Много месаг"
                },
                {
                    "Columns": 1,
                    "Rows": 2,
                    "BgColor": "#e6f5ff",
                    "BgMedia": "http://link.to.button.image",
                    "BgMediaType": "picture",
                    "BgLoop": True,
                    "ActionType": "reply",
                    "ActionBody": "MASS_MESSAGES2",
                    "ReplyType": "message",
                    "Text": "XZ"
                },
            ],
            "InputFieldState": 'regular'
        }
