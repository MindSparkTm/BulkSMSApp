from django.db import models
from accounts.models import UserProfile
# Create your models here.
from django.db.models.signals import post_save,pre_save
from .handler import parse_uploaded_file
class Message(models.Model):

    status_response = (
        ('100','Processed'),
        ('101','Sent'),
        ('102','Queued'),
        ('401','RiskHold'),
        ('402','InvalidSenderId'),
        ('403','InvalidPhoneNumber'),
        ('404','UnsupportedNumberType'),
        ('405','InsufficientBalance'),
        ('406','UserInBlacklist'),
        ('407','CouldNotRoute'),
        ('500','InternalServerError'),
        ('501','GatewayError'),
        ('502', 'RejectedByGateway'),
    )
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='sms_message')
    message_text = models.TextField(null=True,blank=True)
    cost = models.CharField(max_length=20,null=True,blank=True)
    message_Id = models.CharField(max_length=50,null=True,blank=True)
    status = models.CharField(max_length=10,null=True,blank=True)
    status_response = models.CharField(max_length=20,choices=status_response,blank=True,null=True)

    class Meta:
        verbose_name = 'SMS Message'
        verbose_name_plural = 'SMS Messages'

    def __str__(self):
        return u'{}{}'.format(self.user_profile.user.username,self.message_Id)

class FileUpload(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'File Upload'
        verbose_name_plural = 'File Upload'

    def __str__(self):
        return u'{}{}'.format(self.pk,self.description)


def save_profile(sender, instance,created, **kwargs):
    if created:
        print('Instance',instance.pk)
        parse_uploaded_file.s(instance.pk).apply_async(countdown=10)

post_save.connect(save_profile, sender=FileUpload)

