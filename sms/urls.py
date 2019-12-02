from django.conf.urls import url
from .views import BulkUpload
app_name ='sms'
urlpatterns = [
    url(r'^upload/$', BulkUpload.as_view(), name='bulk_upload'),
]