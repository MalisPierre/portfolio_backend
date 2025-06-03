from django.urls import path
from hobby.views import hobby_list, hobby_infos

urlpatterns = [
    path('api/hobby_list', hobby_list, name='hobby-list'),
    path('api/hobby_infos/<int:pk>', hobby_infos, name='hobby-infos'),
]