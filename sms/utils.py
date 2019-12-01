import json
import africastalking
from dotenv import load_dotenv
import os
from accounts.models import UserProfile
from django.shortcuts import get_object_or_404

def send_message(name,recipient_number):
    from .models import Message
    try:
        user_profile = UserProfile.objects.get(phone_number=recipient_number)
    except UserProfile.DoesNotExist:
        print('Phone Number Doesnot exist in Db', recipient_number)
        return str(recipient_number)
    else:
        load_dotenv()
        # username = os.getenv("test_username")  # use 'sandbox' for development in the test environment
        # api_key = os.getenv("test_api_key")  # use your sandbox app API key for development in the test environment
        username = os.getenv("production_username")
        api_key = os.getenv("production_api_key")
        africastalking.initialize(username, api_key)
        if recipient_number:
            recipient_number = u'{}{}'.format('+', recipient_number)
        # Initialize a service e.g. SMS
        sms = africastalking.SMS

        # Use the service synchronously
        message_text = "Rj here.I am Jarvis.Rj's A.I creation.He is my creator.He asked to run a bulk sms simulation for Project Vyaas and added you as one of his favorite recipient"
        response = sms.send(message_text, [recipient_number])
        response = json.dumps(response)
        response = json.loads(response)
        Message.objects.create(status_response=response['SMSMessageData']['Recipients'][0]['statusCode'],
                               message_text=response['SMSMessageData']['Recipients'][0],
                               status=response['SMSMessageData']['Recipients'][0]['status'],
                               message_Id=response['SMSMessageData']['Recipients'][0]['messageId'],
                               user_profile=user_profile,
                               cost=response['SMSMessageData']['Recipients'][0]['cost']
                               )
        print(response['SMSMessageData'])
        print(response['SMSMessageData']['Recipients'][0])
        print(response['SMSMessageData']['Recipients'][0]['statusCode'])
        print(response['SMSMessageData']['Recipients'][0]['number'])
        print(response['SMSMessageData']['Recipients'][0]['cost'])
        print(response['SMSMessageData']['Recipients'][0]['status'])
        print(response['SMSMessageData']['Recipients'][0]['messageId'])
        return str(response['SMSMessageData']['Recipients'][0]['statusCode'])
