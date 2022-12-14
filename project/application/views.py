from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
import africastalking
from django.views.decorators.csrf import csrf_exempt 
# from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword

from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView


@csrf_exempt
def sms(request):
    if request.method =='POST':
        username = ""    # use 'sandbox' for development in the test environment
        api_key = ""  # use your sandbox app API key for development in the test environment
        africastalking.initialize(username, api_key)


        # Initialize a service e.g. SMS
        sms = africastalking.SMS

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['phonenumber']
        # Use the service synchronously
        # response = sms.send("Hello Message!", [content])
        # print(response)

        # Or use it asynchronously
        def on_finish(error, response):
            if error is not None:
                raise error
            print(response)

        sms.send("Car Buyers.Welcome to Accident history checker. Check car accident history, accident locations and major causes of accidents. BEWARE of  the history of second hand car you are buying", [content], callback=on_finish)    


# def getAccessToken(request):
#     consumer_key = '6waG5NUGpbmTu8vOGJbzMAeCVxg9FkSx'
#     consumer_secret = 'Aw0FT6A6sv6GnDeq'
#     api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

#     r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
#     mpesa_access_token = json.loads(r.text)
#     validated_mpesa_access_token = mpesa_access_token['access_token']

#     return HttpResponse(validated_mpesa_access_token)

# @csrf_exempt
# def lipa_na_mpesa_online(request):
#     access_token = MpesaAccessToken.validated_mpesa_access_token
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#     headers = {"Authorization": "Bearer %s" % access_token}
#     request = {
#         "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
#         "Password": LipanaMpesaPpassword.decode_password,
#         "Timestamp": LipanaMpesaPpassword.lipa_time,
#         "TransactionType": "CustomerPayBillOnline",
#         "Amount": 1,
#         "PartyA": 254757612486,
#         "PartyB": LipanaMpesaPpassword.Business_short_code,
#         "PhoneNumber": 254757612486,
#         "CallBackURL": "https://mydomain.com/path",
#         "AccountReference": "Henry",
#         "TransactionDesc": "Testing stk push"
#     }

#     response = requests.post(api_url, json=request, headers=headers)
#     return HttpResponse('success')

# @csrf_exempt
# def MpesaCallBack(request):
#     # logging.info("{}".format("Callback from MPESA"))
#     data = request.body.decode('utf-8')
#     mpesa_payment = json.loads(data)
#     # print("Mpesa Payment")
#     # print(mpesa_payment)
#     # -print(mpesa_payment['FirstName'])
#     # return mpesa_payment
#     return JsonResponse(mpesa_payment)

# # Create your views here.
