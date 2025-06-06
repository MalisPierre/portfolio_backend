# Generated by Django 5.1.7 on 2025-05-14 04:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0003_experience_banner_alter_experience_contract_type'),
        ('skill', '0006_skill_banner_alter_skill_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Experience Description', max_length=100, verbose_name='Description')),
                ('experience', models.ForeignKey(help_text='Experience', on_delete=django.db.models.deletion.CASCADE, to='experience.experience', verbose_name='Experience')),
                ('skill', models.ForeignKey(help_text='Skill', on_delete=django.db.models.deletion.CASCADE, to='skill.skill', verbose_name='Skill')),
            ],
        ),
    ]
