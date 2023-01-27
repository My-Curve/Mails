from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def SendView(request):
    
    if request.method == 'POST':
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        email=request.POST.get('email')
        send_mail(subject,message,settings.EMAIL_HOST_USER,[email])
        return render(request,'sent.html',{'email':email})
    
    
    return render(request,'mail.html')