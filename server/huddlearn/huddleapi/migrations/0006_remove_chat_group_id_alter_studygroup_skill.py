# Generated by Django 5.0 on 2023-12-28 05:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huddleapi', '0005_alter_projectgroup_chat_alter_studygroup_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='group_id',
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='study_groups', to='huddleapi.skill'),
        ),
    ]
