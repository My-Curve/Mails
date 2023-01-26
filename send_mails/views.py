from django.shortcuts import render

# Create your views here.


def SendView(request):
    
    if request.method == 'POST':
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        receiver_mail=request.POST.get('receiver_mail')
    
    context={}
    
    return render(request,'sent.html',context)