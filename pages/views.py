from django.shortcuts import render

# Create your views here.


def contact(request):
    context ={}
    return render(request, 'pages/contact.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

def art(request):
    context={}
    return render(request, 'pages/art.html', context)