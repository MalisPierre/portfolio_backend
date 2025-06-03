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
from skill.models import Skill, SkillMode
from skill.serializer import BasicSkillSerializer, DetailedSkillSerializer


def simple_test(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    users = User.objects.all()
    return render(request,'simple_test.html',
                    {'message': 'tototototo', 'users': users})

@csrf_exempt
@api_view(['GET', 'POST'])
def skill_list(request):
    search = request.data.pop('search', None)
    mode = request.data.pop('mode', None)
    print("MODE == " + str(mode))
    if search:
        skills = Skill.objects.filter(title__contains=search, mode=mode).order_by("-level").only('id', 'title', 'level', 'icon')
    else:
        skills = Skill.objects.filter(mode=mode).order_by("-level").only('id', 'title', 'level', 'icon')
    print(skills)
    serializer = BasicSkillSerializer(skills, many=True)
    return Response(serializer.data, status=200)

# @ensure_csrf_cookie
@csrf_exempt
@api_view(['GET', 'POST'])
def skill_infos(request, pk): 
    print("SKILL ID == " + str(pk))

    skill = Skill.objects.get(pk=pk)
        
    serializer = DetailedSkillSerializer(skill)
    return Response(serializer.data, status=200)

@csrf_exempt
@api_view(['GET', 'POST'])
def send_email(request):

    # data = []
    search = request.data.pop('search', None)

    if search:
        skills = Skill.objects.filter(title__contains=search).order_by("id")
    else:
        skills = Skill.objects.all().order_by("id")

    serializer = BasicSkillSerializer(skills, many=True)
    print("SENDING EMAIL ...")
    from django.core.mail import send_mail
    send_mail("test",
    "test message",
    "malispierre007@gmail.com",
    ["malispierre007@gmail.com",],)
    return Response(serializer.data, status=200)