# Generated by Django 5.0 on 2023-12-28 02:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HuddleUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('picture', models.ImageField(null=True, upload_to='user_pictures/')),
                ('personal_data', models.JSONField()),
                ('public_links', models.JSONField()),
                ('notifications', models.JSONField()),
                ('accountability', models.JSONField()),
                ('skill_levels', models.JSONField()),
                ('settings', models.JSONField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('context', models.TextField(blank=True, null=True)),
                ('reactions', models.JSONField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='huddleapi.chat')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='huddleapi.huddleuser')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(null=True, upload_to='project_pictures/')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('tasks', models.JSONField()),
                ('stage', models.CharField(max_length=255)),
                ('links', models.JSONField()),
                ('resources', models.JSONField()),
                ('open_positions', models.JSONField()),
                ('users_to_skills', models.JSONField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_projects', to='huddleapi.huddleuser')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('picture', models.ImageField(null=True, upload_to='skill_pictures/')),
                ('description', models.TextField()),
                ('resources', models.JSONField()),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_skills', to='huddleapi.huddleuser')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('picture', models.ImageField(null=True, upload_to='project_group_pictures/')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('social_networks_links', models.JSONField()),
                ('users_to_skills', models.JSONField()),
                ('active_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_group', to='huddleapi.project')),
                ('archived_projects', models.ManyToManyField(related_name='group_archived', to='huddleapi.project')),
                ('chat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='huddleapi.chat')),
                ('coordinators', models.ManyToManyField(related_name='project_groups_coordinated', to='huddleapi.huddleuser')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_project_groups', to='huddleapi.huddleuser')),
                ('members', models.ManyToManyField(related_name='project_groups', to='huddleapi.huddleuser')),
                ('users_requests', models.ManyToManyField(related_name='project_group_requested', to='huddleapi.huddleuser')),
                ('skills', models.ManyToManyField(to='huddleapi.skill')),
            ],
        ),
        migrations.AddField(
            model_name='huddleuser',
            name='skills',
            field=models.ManyToManyField(related_name='users_with_skill', to='huddleapi.skill'),
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('picture', models.ImageField(null=True, upload_to='study_group_pictures/')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('social_networks_links', models.JSONField()),
                ('level', models.CharField(blank=True, max_length=255, null=True)),
                ('resources', models.JSONField()),
                ('chat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='huddleapi.chat')),
                ('coordinators', models.ManyToManyField(related_name='study_groups_coordinated', to='huddleapi.huddleuser')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_study_groups', to='huddleapi.huddleuser')),
                ('members', models.ManyToManyField(related_name='study_groups', to='huddleapi.huddleuser')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='huddleapi.skill')),
                ('users_requests', models.ManyToManyField(related_name='study_group_requested', to='huddleapi.huddleuser')),
            ],
        ),
    ]
