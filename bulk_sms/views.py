from django.shortcuts import render,redirect
import africastalking
from .forms import SmsForm

AFRICASTALKING_USERNAME = 'kiash'
AFRICASTALKING_API_KEY='e87eb2bb66083ae1d856081c79bbc0273aa202991c34f0e72f95a957db82e42e'

# Initialize SDK
africastalking.initialize(AFRICASTALKING_USERNAME, AFRICASTALKING_API_KEY)

# Initialize a service e.g. SMS
sms = africastalking.SMS


#use forms
def SmsView(request):
    if request.method == 'POST':
        form = SmsForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            message = form.cleaned_data.get('message')
            
            # Use the service synchronously
            response = sms.send(message, [phone_number])
            print(response)
            #leave it in the smae page of sms
            return redirect('bulk_sms:sms')
    else:
        form = SmsForm()
    return render(request, 'sms.html', {'form': form})
