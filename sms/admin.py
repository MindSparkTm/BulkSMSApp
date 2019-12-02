from django.contrib import admin
from .models import Message,FileUpload
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    def get_username(self,obj):
        return obj.user_profile.user.username
    list_display = ('get_username','message_text','message_Id','status_response',)
    search_fields = ('message_Id',)

class FileUploadAdmin(admin.ModelAdmin):

    list_display = ('description','document','status','failed_phone_numbers_list',)


admin.site.register(Message,MessageAdmin)
admin.site.register(FileUpload,FileUploadAdmin)
