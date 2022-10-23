import email
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import viewsets
from . import models, serializers
from app1.models import Contact
from django.contrib import messages
# Create your views here.

def Hello(request):
    return HttpResponse('Hello Namit Saraswat')

def index(request):
    return render(request, 'index.html' )

def about(request):
    return render(request, 'about.html' )

def login(request):
    return render(request, 'login.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query') 

        contact = Contact(name = name, email = email, phone = phone, query = query ) 
        contact.save()
        messages.success(request, 'Record updated successfully')
        return render(request, 'contact.html')

    elif request.method == "GET":
        return render(request, 'contact.html')
    # else:
    #     return HttpResponse('An Error Occurred')



class StateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StateSerializer
    queryset = models.state.objects.all()
        



# def Hello2(request):
#     return render(request, '')