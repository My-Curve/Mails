from django.urls import path
from .views import SmsView

app_name='bulk_sms'


urlpatterns=[
    path('', SmsView, name='sms'),
]

