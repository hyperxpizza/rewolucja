from django.shortcuts import render, redirect, HttpResponse
from .models import ArtImage
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

def contact(request):
    context ={}
    return render(request, 'pages/contact.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

def art(request):
    images = ArtImage.objects.order_by('uploaded_at')
    context={
        'images':images
    }
    return render(request, 'pages/art.html', context)

def contact_mail(request):
    if request.method =="GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try:
                send_mail(subject,message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header')
            
            return redirect('contact')
    
    context = {
        'form': form
    }

    return render(request, 'pages/contact_mail.html', context)    
