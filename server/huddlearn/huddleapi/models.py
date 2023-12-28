"""
This is a draft of models.py model definition for further Django implementation

"""
from django.db import models

from django.contrib.auth.models import User



class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='skill_pictures/', null=True)
    creator = models.ForeignKey('HuddleUser', on_delete=models.SET_NULL, null=True, related_name='created_skills')
    description = models.TextField(null=True)
    resources = models.JSONField(null=True)

    def related_groups(self) -> ['StudyGroup']:
        # Your method implementation here
        pass


class Chat(models.Model):
    reserved = models.TextField(null=True)
    # Assuming Chat has a one-to-many relationship with Message


# class Group(models.Model):


class StudyGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='study_group_pictures/', null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    social_networks_links = models.JSONField(null=True)
    creator = models.ForeignKey('HuddleUser', on_delete=models.SET_NULL, null=True, related_name='created_study_groups')
    members = models.ManyToManyField('HuddleUser', related_name='study_groups')
    coordinators = models.ManyToManyField('HuddleUser', related_name='study_groups_coordinated')
    users_requests = models.ManyToManyField('HuddleUser', related_name='study_group_requested', blank=True)
    chat = models.OneToOneField(Chat, on_delete=models.SET_NULL, null=True)
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, related_name='study_groups', null=True)
    level = models.CharField(max_length=255, null=True, blank=True)
    resources = models.JSONField(null=True)

    def suggest_users(self):
        # Your method implementation here
        pass

    def request_to_join(self, user: 'HuddleUser'):
        # Your method implementation here
        pass

    def answer_request(self, user: 'HuddleUser', response: bool):
        # Your method implementation here
        pass

    def publish(self, social_networks_id: int, material: dict, publish_locally: bool):
        # Your method implementation here
        pass


class ProjectGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='project_group_pictures/', null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    social_networks_links = models.JSONField(null=True)
    creator = models.ForeignKey('HuddleUser', on_delete=models.SET_NULL, null=True,
                                related_name='created_project_groups')
    members = models.ManyToManyField('HuddleUser', related_name='project_groups')
    coordinators = models.ManyToManyField('HuddleUser', related_name='project_groups_coordinated')
    users_requests = models.ManyToManyField('HuddleUser', related_name='project_group_requested',blank=True)
    chat = models.OneToOneField(Chat, on_delete=models.SET_NULL, null=True)
    active_project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, related_name='project_group')
    skills = models.ManyToManyField(Skill, related_name='project_groups', blank=True)
    users_to_skills = models.JSONField(null=True)
    archived_projects = models.ManyToManyField('Project', related_name='group_archived', blank=True)

    def suggest_users(self):
        # Your method implementation here
        pass

    def request_to_join(self, user: 'HuddleUser'):
        # Your method implementation here
        pass

    def answer_request(self, user: 'HuddleUser', response: bool):
        # Your method implementation here
        pass

    def publish(self, social_networks_id: int, material: dict, publish_locally: bool):
        # Your method implementation here
        pass

    def new_project(self):
        # Your method implementation here
        pass

    def select_project(self, project: 'Project'):
        # Your method implementation here
        pass

    def transfer_project(self, project: 'Project', other_group: 'ProjectGroup'):
        # Your method implementation here
        pass


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='project_pictures/', null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    tasks = models.JSONField(null=True)
    stage = models.CharField(max_length=255)
    links = models.JSONField(null=True)
    resources = models.JSONField(null=True)
    open_positions = models.JSONField(null=True)
    users_to_skills = models.JSONField(null=True)
    creator = models.ForeignKey('HuddleUser', on_delete=models.SET_NULL, null=True, related_name='created_projects')

    def assign_task(self, task: str):
        # Your method implementation here
        pass

    def submit_task(self, task: str):
        # Your method implementation here
        pass

    def update_stage(self, new_stage: str):
        # Your method implementation here
        pass


class Message(models.Model):
    title = models.CharField(max_length=255)
    datetime_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('HuddleUser', on_delete=models.SET_NULL, null=True, related_name='messages')
    context = models.TextField(null=True, blank=True)
    reactions = models.JSONField(null=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')

    def add_reaction(self, user: 'HuddleUser', reaction: str):
        # Your method implementation here
        pass

    def modify_reaction(self, user: 'HuddleUser', reaction: (str | None)):
        # Your method implementation here
        pass


class HuddleUser(models.Model):
    # because we have ManyToMany(User,) relations with other entities ,we have a User.groups attribute, 
    # and also groups_coordinated, group_requested,created_groups
    # created_skills, created_projects and messages

    # this fielsd are in User class:
    # username = models.CharField(max_length=255)
    # email = models.EmailField(unique=True)
    # password = models.CharField(max_length=255)

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # link to Auth User model

    fullname=models.CharField(max_length=255)
    picture = models.ImageField(upload_to='user_pictures/', null=True)
    personal_data = models.JSONField(null=True)
    public_links = models.JSONField(null=True)
    notifications = models.JSONField(null=True)
    accountability = models.JSONField(null=True)
    skills = models.ManyToManyField(Skill, related_name='users_with_skill', blank=True)
    skill_levels = models.JSONField(null=True)
    settings = models.JSONField(null=True)

    def validate_password(self, password: str):
        pass

    def search_for_group(self, query):
        # Your method implementation here
        pass

    def search_for_project(self, query):
        # Your method implementation here
        pass

    def create_study_group(self, group: StudyGroup):
        # Your method implementation here
        pass

    def create_project_group(self, group: ProjectGroup):
        # Your method implementation here
        pass

    def create_project(self, project: Project):
        # Your method implementation here
        pass