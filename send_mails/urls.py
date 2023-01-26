from django.urls import path
from .views import SendView
app_name='sendmails'

urlpatterns=[
    path('',SendView,name='sent')
]