# Generated by Django 5.0 on 2023-12-29 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huddleapi', '0009_remove_studygroup_skills_studygroup_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studygroup',
            name='skill',
        ),
        migrations.AddField(
            model_name='studygroup',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='study_groups', to='huddleapi.skill'),
        ),
    ]