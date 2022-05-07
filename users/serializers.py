from django.db import transaction
from django.contrib.auth.password_validation import validate_password, get_password_validators
from django.conf import settings

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User




class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
                validators=[UniqueValidator(queryset=User.objects.all(),
                message='User with this email already exists', lookup='iexact')])
    password = serializers.CharField(min_length=8, write_only=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


    def validate_password(self, value):
        try:
            validate_password(
                password=value,
                password_validators=get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
            )
            return value
        except Exception as e:
            raise serializers.ValidationError(e) 



    
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name',]
		# read_only_fields = [ 'last_login', 'is_active','id', ]

    def create(self, validated_data):
   
        with transaction.atomic():
            user = User.objects.create(**validated_data)
     
        return user