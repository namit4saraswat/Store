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

def contact(request):
    if request == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query') 

    contact = Contact(name = name, email=email, phone= phone, query= query ) 
    contact.save()
    messages.add_message(request, messages.INFO, 'Record Uploaded')
    return render(request, 'contact.html' )



class StateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StateSerializer
    queryset = models.state.objects.all()
        



# def Hello2(request):
#     return render(request, '')