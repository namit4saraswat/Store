from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework import viewsets
from . import models, serializers
# Create your views here.

def Hello(request):
    return HttpResponse('Hello Namit Saraswat')

class StateViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StateSerializer
    queryset = models.state.objects.all()
        



# def Hello2(request):
#     return render(request, '')