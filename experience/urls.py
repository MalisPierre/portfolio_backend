from django.urls import path
from experience.views import experience_list, experience_infos

urlpatterns = [
    path('api/experience_list', experience_list, name='experience-list'),
    path('api/experience_infos/<int:pk>', experience_infos, name='experience-infos'),
]