
from django.shortcuts import render
from .models import Set
from rest_framework import viewsets, permissions
from .serializers import SetSerializer



class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SetSerializer









# def index(request):
  
#     name=Surname.objects.order_by()
#     return render(request, 'website/surname_list.html',{'name': name })


# def detail(request,pk):
#     return ( request, Surname , pk:=id)

# # test