from django.conf.urls import url
from django.urls import path
from . import views

app_name='pages'

urlpatterns =[
    path('art', views.art, name='art'),
    path('contact/', views.contact, name='contact'),
    path('', views.about, name='about')
]