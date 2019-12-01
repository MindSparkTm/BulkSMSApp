from django.shortcuts import render,HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View,CreateView
import json
import africastalking
from .models import FileUpload
# Create your views here.
from dotenv import load_dotenv
import os
import pandas as pd


class BulkUpload(CreateView):
    model = FileUpload
    fields = ('description','document')
    success_url = reverse_lazy('sms:bulk_upload')

def SendSms(View):
    load_dotenv()
    username = os.getenv("test_username")   # use 'sandbox' for development in the test environment
    api_key = os.getenv("test_api_key")  # use your sandbox app API key for development in the test environment

    africastalking.initialize(username, api_key)

    # Initialize a service e.g. SMS
    sms = africastalking.SMS

    # Use the service synchronously
    response = sms.send("Hello Message!", ["+254720323306"])
    print(response)
    response = json.dumps(response)
    response = json.loads(response)
    print(response['SMSMessageData'])
    print(response['SMSMessageData']['Recipients'][0])
    print(response['SMSMessageData']['Recipients'][0]['statusCode'])
    print(response['SMSMessageData']['Recipients'][0]['number'])
    print(response['SMSMessageData']['Recipients'][0]['cost'])
    print(response['SMSMessageData']['Recipients'][0]['status'])
    print(response['SMSMessageData']['Recipients'][0]['messageId'])
    return HttpResponse('success')



