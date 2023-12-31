# Generated by Django 5.0 on 2023-12-28 05:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huddleapi', '0004_chat_group_id_chat_reserved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectgroup',
            name='chat',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='huddleapi.chat'),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='chat',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='huddleapi.chat'),
        ),
    ]
