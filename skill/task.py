from django.contrib import admin
from django.shortcuts import redirect, render
from adminplus.sites import AdminSitePlus
from django.urls import reverse
from skill.models import Skill, SkillSection
from time import sleep
# from celery import shared_task

# @shared_task()
def task_clear_database():
    # from time import sleep
    from experience.models import Experience, ExperienceSkill, ExperienceTask
    from diploma.models import Diploma
    from hobby.models import Hobby, HobbyImage
    print("START CLEARING UP DATABASE")
    skills = Skill.objects.all()
    skills.delete()
    sections = SkillSection.objects.all()
    sections.delete()
    experiences = Experience.objects.all()
    experiences.delete()
    experience_skills = ExperienceSkill.objects.all()
    experience_skills.delete()
    experience_stasks = ExperienceTask.objects.all()
    experience_stasks.delete()
    hobbies = Hobby.objects.all()
    hobbies.delete()
    hobby_images = HobbyImage.objects.all()
    hobby_images.delete()
    diplomas = Diploma.objects.all()
    diplomas.delete()
    print("DONE CLEARING UP DATABASE")

# @shared_task()
def task_populate_database():
    from django.core.management import call_command
    print("STARTING POPULATING DATABASE ...")
    call_command('loaddata', 'core/fixtures/skills.json', verbosity=0)
    call_command('loaddata', 'core/fixtures/experiences.json', verbosity=0)
    call_command('loaddata', 'core/fixtures/hobbies.json', verbosity=0)
    print("DONE POPULATING DATABASE")