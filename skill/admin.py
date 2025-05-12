from django.contrib import admin
from skill.models import Skill, SkillSection
from django.shortcuts import redirect, render
from adminplus.sites import AdminSitePlus
from django.contrib.auth.models import User, Group
from skill.task import task_clear_database, task_populate_database

admin.site = AdminSitePlus()

admin.site.register(User)
admin.site.register(Group)

admin.site.register(Skill)
admin.site.register(SkillSection)

def clear_database(request, *args, **kwargs):
    from django.core.management import call_command
    if request.method == 'GET':
        return render(request=request, template_name="admin/basic_action.html", context={
            "title": "Nettoyer la base de donnée", 
            "url": "/adm/clear_database",
            "question": "Etes vous sur de vouloir vider la base de donnée ?"
        })
    else:
        task_clear_database()
        return redirect('/adm')


def populate_database(request, *args, **kwargs):
    from django.core.management import call_command
    if request.method == 'GET':
        return render(request=request, template_name="admin/basic_action.html", context={
            "title": "Populer la base de donnée", 
            "url": "/adm/populate_database",
            "question": "Etes vous sur de vouloir populer la base de donnée ?"
        })
    else:
        task_populate_database()
        return redirect('/adm')

admin.site.register_view('clear_database', view=clear_database, name='clear database')
admin.site.register_view('populate_database', view=populate_database, name='populate database')