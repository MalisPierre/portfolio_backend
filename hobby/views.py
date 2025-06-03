from django.shortcuts import render

# Create your views here.
from hobby.models import Hobby
from hobby.serializer import BasicHobbySerializer, DetailedHobbySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST'])
def hobby_list(request):
    search = request.data.pop('search', None)

    if search:
        hobbys = Hobby.objects.filter(title__contains=search).order_by("id")
    else:
        hobbys = Hobby.objects.all().order_by("id")

    serializer = BasicHobbySerializer(hobbys, many=True)
    return Response(serializer.data, status=200)
    

# @ensure_csrf_cookie
@csrf_exempt
@api_view(['GET', 'POST'])
def hobby_infos(request, pk): 
    print("ID == " + str(pk))

    hobby = Hobby.objects.get(pk=pk)
        
    serializer = DetailedHobbySerializer(hobby)
    return Response(serializer.data, status=200)