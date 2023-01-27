from django.shortcuts import render

# Create your views here.
def SmsView(request):
    return render(request, 'sms.html')