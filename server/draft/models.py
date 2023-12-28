"""
This is a draft of models.py model definition for further Django implementation

"""
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    picture = models.ImageField(upload_to='skill_pictures/', null=True)
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='created_skills')
    description = models.TextField()
    resources = models.JSONField()

    def related_groups(self)->['Group']:
        # Your method implementation here
        pass


class Chat(models.Model):
    # Assuming Chat has a one-to-many relationship with Message
    pass


class Group(models.Model):
    GROUP_TYPE_CHOICES = [
        ('study', 'Study Group'),
        ('project', 'Project Group'),
    ]
    name = models.CharField(max_length=255, unique=True)
    group_type = models.CharField(max_length=10, choices=GROUP_TYPE_CHOICES)
    picture = models.ImageField(upload_to='group_pictures/', null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    social_networks_links = models.JSONField()
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='created_groups')
    members = models.ManyToManyField('User', related_name='groups')
    coordinators = models.ManyToManyField('User', related_name='groups_coordinated')
    users_requests = models.ManyToManyField('User', related_name='group_requested')
    chat = models.OneToOneField(Chat, on_delete=models.CASCADE)

    def suggest_users(self):
        # Your method implementation here
        pass

    def request_to_join(self, user:'User'):
        # Your method implementation here
        pass

    def answer_request(self, user:'User', response:bool):
        # Your method implementation here
        pass

    def publish(self, social_networks_id:int, material:dict, publish_locally:bool):
        # Your method implementation here
        pass


class StudyGroup(Group):
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)
    level = models.CharField(max_length=255, null=True, blank=True)
    resources = models.JSONField()


class ProjectGroup(Group):
    active_project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True, related_name='group')
    skills = models.ManyToManyField(Skill)
    users_to_skills = models.JSONField()
    archived_projects = models.ManyToManyField('Project', related_name='group_archived' )

    def new_project(self):
        # Your method implementation here
        pass

    def select_project(self, project:'Project'):
        # Your method implementation here
        pass

    def transfer_project(self, project:'Project', other_group:'ProjectGroup'):
        # Your method implementation here
        pass


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='project_pictures/', null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    tasks = models.JSONField()
    stage = models.CharField(max_length=255)
    links = models.JSONField()
    resources = models.JSONField()
    open_positions = models.JSONField()
    users_to_skills = models.JSONField()
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='created_projects')

    def assign_task(self, task:str):
        # Your method implementation here
        pass

    def submit_task(self, task:str):
        # Your method implementation here
        pass

    def update_stage(self, new_stage:str):
        # Your method implementation here
        pass


class Message(models.Model):
    title = models.CharField(max_length=255)
    datetime_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='messages')
    context = models.TextField(null=True, blank=True)
    reactions = models.JSONField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')

    def add_reaction(self, user:'User', reaction:str):
        # Your method implementation here
        pass

    def modify_reaction(self,user:'User', reaction:(str|None)):
        # Your method implementation here
        pass


class User(models.Model):
    # because we have ManyToMany(User,) relations with other entities ,we have a User.groups attribute, 
    # and also groups_coordinated, group_requested,created_groups
    # created_skills, created_projects and messages
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='user_pictures/', null=True)
    personal_data = models.JSONField()
    public_links = models.JSONField()
    notifications = models.JSONField()
    accountability = models.JSONField()
    skills = models.ManyToManyField(Skill, related_name='user_skills')
    skill_levels = models.JSONField()
    settings = models.JSONField()
    
    def validate_password(self, password:str):
        pass


    def search_for_group(self, query):
        # Your method implementation here
        pass

    def search_for_project(self, query):
        # Your method implementation here
        pass

    def create_group(self, group:Group):
        # Your method implementation here
        pass
    
    def create_project(self, project:Project):
        # Your method implementation here
        pass