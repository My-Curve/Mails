from django.shortcuts import render
from .api import username, api_key
import africastalking

# Create your views here.
def SmsView(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        phone_number = request.POST.get('phone_number')
        # Initialize SDK
        africastalking.initialize(username, api_key)
        # Initialize a service e.g. SMS
        sms = africastalking.SMS
        # Use the service synchronously
        response = sms.send(message, [phone_number])
        print(response)
        return render(request, 'sms.html')
    return render(request, 'sms.html')