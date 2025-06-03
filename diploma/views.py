from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view
from diploma.models import Diploma
from diploma.serializer import DiplomaSerializer



@csrf_exempt
@api_view(['GET', 'POST'])
def diploma_list(request):
    search = request.data.pop('search', None)

    if search:
        diplomas = Diploma.objects.filter(title__contains=search).order_by("date")
    else:
        diplomas = Diploma.objects.all().order_by("date")

    serializer = DiplomaSerializer(diplomas, many=True)
    return Response(serializer.data, status=200)
    