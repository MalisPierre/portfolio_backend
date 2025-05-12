from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def simple_test(request):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    users = User.objects.all()
    return render(request,'simple_test.html',
                    {'message': 'tototototo', 'users': users})