from rest_framework import serializers, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer

from authApp.serializers.userSerializer import UserSerializer


class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {
            "username": request.data["username"],
            "password": request.data["password"]
        }
        tokenSerializer = TokenObtainSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_excepetion=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
