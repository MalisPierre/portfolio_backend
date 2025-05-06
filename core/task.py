from django.contrib import admin
from django.shortcuts import redirect, render
from adminplus.sites import AdminSitePlus
from django.urls import reverse
from skill.models import Skill, SkillSection
from time import sleep
# from celery import shared_task

# @shared_task()
def task_clear_database():
    from time import sleep
    print("STARTING CLEARING UP DATABASE ...")
    skills = Skill.objects.all()
    for skill in skills:
        skills.delete()
    print("DONE CLEARING UP DATABASE")

# @shared_task()
def task_populate_database():
    from django.core.management import call_command
    print("STARTING POPULATING DATABASE ...")
    call_command('loaddata', 'core/fixtures/skills.json', verbosity=0)
    print("DONE POPULATING DATABASE")