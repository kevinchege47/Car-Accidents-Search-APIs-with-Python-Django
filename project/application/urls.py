from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .apiviews import *
# from .apiviews import PollViewSet

router = DefaultRouter()


urlpatterns = [
	
	# path("createdoctor/", DoctorList.as_view(), name="create_doctor"),
    # path("allergies/<str:pk>/", AllergiesList.as_view(), name="createallergy"),
    # path("illnesses/", illnessesList.as_view(), name="illness"),
    # path("patient/", PatientList.as_view(), name="patient"),

]

urlpatterns += router.urls