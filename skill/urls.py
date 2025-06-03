from django.urls import path
from skill.views import simple_test, skill_list, skill_infos

urlpatterns = [
    path('test', simple_test,name='simple-test'),
    path('api/skill_list', skill_list, name='skill-list'),
    path('api/skill_infos/<int:pk>', skill_infos, name='skill-infos'),
]