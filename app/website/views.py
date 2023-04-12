from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Surname



def index(request):
    templates_name='website/surname_list.html'
    name=Surname.objects.order_by(
        
    )
    return render(request, 'website/surname_list.html',{'name': name })


# def detail(request,Surname_id):
#     return (Surname, id= Surname_id)