from django.contrib.auth import get_user_model
from django.shortcuts import HttpResponse
User = get_user_model()
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import permissions
from .models import UserCheck
from .models import UserData
import logging
import json

logger = logging.getLogger(__name__)


class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        password = data['password']
        password2 = data['password2']
        user_type = data['user_type']

        if password == password2:
            if User.objects.filter(name=name).exists():
                raise serializers.ValidationError({'error': 'User already exists'})
            else:
                if len(password) < 2:
                    raise serializers.ValidationError({'error': 'Password must be greater than 2'})
                else:
                    user = User.objects.create_user(name=name, password=password)
                    UserCheck.objects.create(user_type=user_type, user=user)
                    return Response({'success': 'user created successfully'})
        else:
            raise serializers.ValidationError({'error': 'Passwords does not match'})


class UsercheckView(APIView):
    def post(self, request, format=None):
        data = self.request.data
        try:
            user_type = UserCheck.objects.get(user__name__iexact=data['name']).user_type
            return Response({'type': f'{user_type}'})
        except:
            return Response({'error': 'Error in detecting type of user'})


class UserDataView(APIView):
    def post(self, request, format=None):
        data = self.request.data
        try:
            # user_total = UserData.objects.get(user__name__iexact=data['name']).user_total
            user_total =UserData.objects.get(user_name=data['name']).user_total
            # return Response({'userTotal': f'{user_total}'})
            return HttpResponse(json.dumps(user_total), content_type='application/json')
        except:
            return Response({'error': 'Error in detecting type of user'})
