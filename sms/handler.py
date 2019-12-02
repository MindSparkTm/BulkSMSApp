import pandas as pd
from django.conf import settings
from celery import shared_task
from .utils import send_message
from django.core.mail import send_mail
import logging
logger = logging.getLogger(__name__)

@shared_task
def parse_uploaded_file(file_upload_id):
    from sms.models import FileUpload
    try:
        file_upload = FileUpload.objects.get(id=file_upload_id)
        file_upload.status = FileUpload.STARTED
        file_upload.save()
        file_path = u'{}/{}'.format(settings.MEDIA_URL,str(file_upload.document))
        bulk_sms_record = pd.read_csv(file_path)
        phone_number = bulk_sms_record['phone_number']
        name = bulk_sms_record['name']
        file_upload.upload_status = FileUpload.IN_PROGRESS
        file_upload.save()
        i=0
        failed_phone_numbers = []
        for number in phone_number:
            response = send_message(name[i],number)
            print(response)
            if response.startswith('254'):
                failed_phone_numbers.append(response)
            i+=1
        #this is where you send email message to the client with the numbers of the recipient that didnot work'
        file_upload.status = FileUpload.COMPLETED
        if failed_phone_numbers:
            file_upload.failed_phone_numbers_list = failed_phone_numbers
        file_upload.save()
        return

    # except FileUpload.DoesNotExist:
    #     print("Parse Upload File Exception %d.", "Phone Number Doesn't exist")
    # except FileUpload.MultipleObjectsReturned:
    #     print("Parse Upload File Exception %d.","Multiple Objects Returned ")
    except Exception as ex:
        print("Parse Upload File Exception", str(ex))
        return

def send_email(subject,message_body,sender_email,recipient_list):
    send_mail(
        subject,
        message_body,
        sender_email,
        recipient_list,
        fail_silently=False,
    )
    return

