from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets
from .models import *
from .serializers import CarsSerializer, AccidentsSerializer,InsuranceCompanySerializer


# class CarList(generics.ListCreateAPIView):
# 	def get_queryset(self):
# 		queryset = Cars.objects.all()
# 		filter_backends = [SearchFilter]
# 		search_fields = ['accidents__id','numberplate']
# 		return queryset
# 	serializer_class = CarsSerializer

class CarList(generics.ListCreateAPIView):
	
    queryset = Cars.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['accidents__id','numberplate']
        # queryset = Allergies.objects.get(id=pk)
        # return queryset
    serializer_class = CarsSerializer

class AccidentList(generics.ListCreateAPIView):
	def get_queryset(self):
		queryset = Accidents.objects.all()
        # queryset = Allergies.objects.get(id=pk)
		return queryset
	serializer_class = AccidentsSerializer
    
class insuranceList(generics.ListCreateAPIView):
	def get_queryset(self):
		queryset = InsuranceCompany.objects.all()
        # queryset = Allergies.objects.get(id=pk)
		return queryset
	serializer_class = InsuranceCompanySerializer 

class SingleCar(RetrieveAPIView):
    def get_queryset(self):
        queryset = Cars.objects.all()
        return queryset
    serializer_class = CarsSerializer

