from django.contrib import admin
from hobby.models import Hobby, HobbyImage
from django.shortcuts import redirect, render
from adminplus.sites import AdminSitePlus
from django.contrib.auth.models import User, Group
from skill.task import task_clear_database, task_populate_database


admin.site.register(Hobby)
admin.site.register(HobbyImage)