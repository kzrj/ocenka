# # -*- coding: utf-8 -*-
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

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

from jobs.models import Job, Category
from jobs.serializers import JobSerializer, JobFirstCreateSerializer, CategorySerializer
from jobs.testing_utils import create_test_jobs
from jobs.filters import JobFilter
from clients.models import Profile
from core.utils import create_token


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_class = JobFilter

    # def get_serializer_class(self):
    #     print('get_serializer')
    #     return super(JobViewSet, self).get_serializer_class()

    def get_serializer_class(self):
        print('get_serializer_class')
        print(self.action)
        if self.action == 'first_create':
            print('get_serializer_class first_create')
            return JobFirstCreateSerializer
        return JobSerializer

    @action(methods=['post'], detail=False, name='first_create', serializer_class=JobFirstCreateSerializer)
    def first_create(self, request):
        serializer = JobFirstCreateSerializer(data=request.data)
        if serializer.is_valid():
            # get or create profile
            profile = request.user.profile
            profile.nickname = serializer.validated_data['name']
            profile.phone = serializer.validated_data['phone']
            profile.mark_as_zakazchik()

            job = Job.objects.create_job(
                title=serializer.validated_data['title'],
                category=serializer.validated_data['category'],
                budget=serializer.validated_data['budget'],
                address=serializer.validated_data['address'],
                zakazchik=profile,
                description=serializer.validated_data['description'],
                start_date=serializer.validated_data['start_date'],
                end_date=serializer.validated_data['end_date']
                )
            return Response(
                {
                    "message": "Created"
                },
                status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InitTestDataView(APIView):
    def get(self, request, format=None):
        create_test_jobs()
        return Response({'msg': 'Done.'})


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


@csrf_exempt
def viber_view(request):
    viber_request = viber.parse_request(request.body)

    text_message = TextMessage(text="Оппа!")
    msgs = [text_message for i in range(0, 10)]

    if isinstance(viber_request, ViberConversationStartedRequest):
        viber_user = viber_request.user

        text_message = TextMessage(text="Конверсэйшн! Приветствие! Логин!", trackingData='FIRST_LOGIN')
        viber.send_messages(viber_request.user.id, [
            text_message, 
            # KeyboardMessage(tracking_data='TRACKING_CREATE_AD_PHONE', 
            #                 keyboard=login_keyboard(viber_request.user.id),
            #                 min_api_version=6)
        ])
    else:
        viber_user = viber_request.sender

    customer = Profile.objects.get_or_create_profile_viber(
            viber_id=viber_user.id,
            viber_name=viber_user.name,
            viber_avatar=viber_user.avatar,
            )

    if isinstance(viber_request, ViberUnsubscribedRequest):
        return HttpResponse('ok', status=200)

    if viber_request.message.text == 'MASS_MESSAGES':
        for i in range(0, 10):
            viber.send_messages(viber_request.sender.id, [
                text_message
            ])
    elif viber_request.message.text == 'MASS_MESSAGES2':
        viber.send_messages(viber_request.sender.id, msgs)
    else:
        # text_message = TextMessage(text="Оппа!")
        # viber.send_messages(viber_request.sender.id, msgs)
        url_message = URLMessage(media="https://svoyaeda.su/api/");
        token = create_token(customer.user)
        viber.send_messages(viber_request.sender.id, [
            text_message, url_message,
            KeyboardMessage(tracking_data='TRACKING_CREATE_AD_PHONE', 
                            keyboard=login_keyboard(token),
                            min_api_version=6)
        ])

    return HttpResponse('ok', status=200)