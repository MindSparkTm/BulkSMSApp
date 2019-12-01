from django.conf.urls import url
from .views import SendSms,BulkUpload
app_name ='sms'
urlpatterns = [
    url(r'^message/$',SendSms,name='send_sms'),
    url(r'^upload/$', BulkUpload.as_view(), name='bulk_upload'),

]