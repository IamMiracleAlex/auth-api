from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from users.utils import jwt_token
from users.serializers import UserLoginSerializer, UserSerializer 
from users.models import  User


class LoginView(APIView):
    '''
    Login users
    POST /users/login/
    '''
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=UserLoginSerializer, responses={200: UserSerializer} )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")

        user = authenticate(email=email, password=password)
        if not user:
            return Response(
				data={'detail':'Invalid credentials'},
				status=status.HTTP_401_UNAUTHORIZED
            )

        login(request, user)

     
        data = UserSerializer(user).data
        
        data['token'] = jwt_token(user)

        return Response(data={'detail':'Login successful', 'data': data})


class LogoutView(APIView):
    '''
    Log out users
    POST /users/logout/
    '''
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={204: None} )
    def post(self, request, format=None):
        logout(request)
      
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class SignUpView(APIView):
    '''
    Create new user accounts
    POST /users/signup/
    '''
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=UserSerializer, responses={201: UserSerializer} )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
                 
        return Response(data={
				'detail':'User created successfully',
		  		'data':serializer.data,
		  		},
                status=status.HTTP_201_CREATED
            )
				