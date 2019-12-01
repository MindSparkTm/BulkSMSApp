import pandas as pd
from django.conf import settings
from celery import shared_task
from .utils import send_message
from django.core.mail import send_mail

import re
@shared_task
def parse_uploaded_file(file_upload_id):
    from sms.models import FileUpload
    try:
        file_upload = FileUpload.objects.get(id=file_upload_id)
        file_path = settings.MEDIA_URL+'/'+str(file_upload.document)
        bulk_sms_record = pd.read_csv(file_path)
        phone_number = bulk_sms_record['phone_number']
        name = bulk_sms_record['name']
        i=0
        failed_phone_numbers = []
        for number in phone_number:
            response = send_message(name[i],number)
            print(response)
            if response.startswith('254'):
                failed_phone_numbers.append(response)
            i+=1
        #this is where you send email message to the client with the numbers of the recipient that didnot work'
        message_body = ",".join(failed_phone_numbers)
        send_email('Failed Phone Number List',message_body,'smartsurajit2008@gmail.com',
                   ['smartsurajit2008@gmail.com','surajit@mumsvillage.com'])
    except Exception as ex:
        print('exception',ex)

def send_email(subject,message_body,sender_email,recipient_list):
    send_mail(
        subject,
        message_body,
        sender_email,
        recipient_list,
        fail_silently=False,
    )

