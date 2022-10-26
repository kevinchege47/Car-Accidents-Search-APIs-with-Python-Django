from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import *

class AccidentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Accidents
		fields = '__all__'

class InsuranceCompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = InsuranceCompany
		fields = '__all__'

class CarsSerializer(serializers.ModelSerializer):
    accidents = AccidentsSerializer(read_only=True,many=True)
    insurancecompany = InsuranceCompanySerializer(read_only = True,many=True)
    class Meta:
        model = Cars
        fields = '__all__'
