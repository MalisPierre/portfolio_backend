from django.http import HttpResponse
from django.shortcuts import render

def simple_test(request):
    return render(request,'simple_test.html',
                    {'user_name': 'tototototo'})