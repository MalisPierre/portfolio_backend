# Generated by Django 5.1.7 on 2025-05-18 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0009_skill_example_skill_tips_alter_skill_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='color',
            field=models.TextField(blank=True, help_text='Skill Color for Banner', max_length=6, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='skill',
            name='display_title',
            field=models.BooleanField(default=False, help_text='Should we display the skill title ?', verbose_name='Display Title'),
        ),
    ]
