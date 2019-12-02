from django.shortcuts import render, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, CreateView
import json
import africastalking
from .models import FileUpload


# Create your views here.


class BulkUpload(CreateView):
    model = FileUpload
    fields = ('description', 'document')
    success_url = reverse_lazy('sms:bulk_upload')
