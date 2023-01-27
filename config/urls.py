
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('send_mails.urls',namespace='send_mails')),
    path('bulk_sms/',include('bulk_sms.urls',namespace='bulk_sms'))
]
