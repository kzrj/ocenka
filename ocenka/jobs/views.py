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

from jobs.models import Job, Category, JobImage
from jobs.serializers import JobSerializer, JobFirstCreateSerializer, CategorySerializer, \
     JobUpdateSerializer, JobDeactivateSerializer, JobImageCreateSerializer, JobImageSerializer, \
     JobImageIdSerializer, JobFullSerializer
from jobs.testing_utils import create_test_jobs
from jobs.filters import JobFilter
from jobs.pagination import JobPagination
from clients.models import Profile
from core.utils import create_token
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    filter_class = JobFilter
    pagination_class = JobPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return JobFullSerializer
        if self.action == 'create':
            return JobUpdateSerializer
        if self.action == 'partial_update':
            return JobUpdateSerializer
        return self.serializer_class

    def list(self, request):
        queryset = self.filter_queryset(
            self.get_queryset()
        )
        category_serializer = CategorySerializer(Category.objects.all(), many=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = JobSerializer(page, many=True)
            return self.get_paginated_response({'jobs': serializer.data,
                'categories': category_serializer.data})

        serializer = JobSerializer(queryset, many=True)
        return Response({
            'jobs': serializer.data,
            'categories': category_serializer.data
        })

    def create(self, request):
        serializer = JobUpdateSerializer(data=request.data)
        if serializer.is_valid():
            # get or create profile
            profile = request.user.profile
            job = Job.objects.create_job_and_mailing(
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

    def destroy(self, request, pk=None):
        pass

    @action(methods=['post'], detail=False, serializer_class=JobFirstCreateSerializer)
    def first_create(self, request):
        serializer = JobFirstCreateSerializer(data=request.data)
        if serializer.is_valid():
            # get or create profile
            profile = request.user.profile
            profile.nickname = serializer.validated_data['name']
            profile.phone = serializer.validated_data['phone']
            profile.mark_as_zakazchik()

            job = Job.objects.create_job_and_mailing(
                title=serializer.validated_data['title'],
                category=serializer.validated_data['category'],
                budget=serializer.validated_data['budget'],
                address=serializer.validated_data['address'],
                zakazchik=profile,
                description=serializer.validated_data['description'],
                start_date=serializer.validated_data['start_date'],
                end_date=serializer.validated_data['end_date'],
                )
            return Response(
                {
                    "message": "Created"
                },
                status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, serializer_class=JobDeactivateSerializer)
    def activate_deactivate(self, request, pk=None):
        serializer = JobDeactivateSerializer(data=request.data)
        if serializer.is_valid():
            job = self.get_object()
            job.active = serializer.validated_data['active']
            job.save()
            return Response(
                {
                    "message": "Работа активна" if serializer.validated_data['active'] else "Работа неактивна"
                },
                status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['post'], detail=True, serializer_class=JobImageCreateSerializer)
    def add_image(self, request, pk=None):
        serializer = JobImageCreateSerializer(data=request.data)
        if serializer.is_valid():
            job = self.get_object()
            job.images.create_job_image(image_file=serializer.validated_data['original'], job=job)
            
            return Response(
                {
                    "job": JobSerializer(job).data,
                    "message": "Изображение добавлено."
                },
                status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, serializer_class=JobImageIdSerializer)
    def delete_image(self, request, pk=None):
        serializer = JobImageIdSerializer(data=request.data)
        if serializer.is_valid():
            job = self.get_object()
            image = serializer.validated_data['image']
            image.delete()
            
            return Response(
                {
                    "job": JobSerializer(job).data,
                    "message": "Изображение удалено."
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

# url='https://svoyaeda.su'

def login_keyboard(viber_id=None, url='http://192.168.1.3:3000'):
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
                    "ActionBody": f"{url}/dm/login/v/{viber_id}",
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

        text_message = TextMessage(text="Конверсэйшн! Приветствие! Логин!")
        viber.send_messages(viber_request.user.id, [
            text_message, 
            KeyboardMessage(
                # tracking_data='TRACKING_CREATE_AD_PHONE', 
                keyboard=login_keyboard(123),
                min_api_version=6)
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