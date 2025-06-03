from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
import json

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from experience.models import Experience
from experience.serializer import BasicExperienceSerializer, DetailedExperienceSerializer



@csrf_exempt
@api_view(['GET', 'POST'])
def experience_list(request):
    search = request.data.pop('search', None)

    if search:
        experiences = Experience.objects.filter(title__contains=search).order_by("-start_date")
    else:
        experiences = Experience.objects.all().order_by("-start_date")

    serializer = BasicExperienceSerializer(experiences, many=True)
    return Response(serializer.data, status=200)
    

# @ensure_csrf_cookie
@csrf_exempt
@api_view(['GET', 'POST'])
def experience_infos(request, pk): 

    experience = Experience.objects.get(pk=pk)
        
    serializer = DetailedExperienceSerializer(experience)
    return Response(serializer.data, status=200)