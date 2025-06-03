from django.urls import path
from diploma.views import diploma_list

urlpatterns = [
    path('api/diploma_list', diploma_list, name='diploma-list'),
]