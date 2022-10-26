from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .apiviews import *
# from .apiviews import PollViewSet

router = DefaultRouter()


urlpatterns = [

	
	path("createcar/", CarList.as_view(), name="create_car"),
    path("accidents/<str:pk>/", AccidentList.as_view(), name="createallergy"),
    path("insurance/", insuranceList.as_view(), name="insurance"),
    path('accesstoken/', views.getAccessToken, name='get_mpesa_access_token'),
    path('onlinelipa/', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    

]

urlpatterns += router.urls