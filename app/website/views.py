from django.shortcuts import render
from django.http import HttpResponse
from django.utils import  timezone
from .models import Surname



def index(request):
  
    name=Surname.objects.filter( pub_date__lte=timezone.now()
        
    ).order_by('-pub-date')
    return render(request, 'website/surname_list.html',{'name': name })


def detail(request,pk):
    return ( request, Surname , pk:=id)

# test