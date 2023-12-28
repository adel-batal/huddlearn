"""
This is a draft of python code, build for demonstration purposes from the Class Diagram
More work has been done on Django models.py file, and the work will continue there

But this code is more simpler, so may be easy to understand 
and see class structure and relations 

"""
class Skill:
    def __init__(self, name, picture=None, creator=None, description='', resources=None):
        self.name = name
        self.picture = picture
        self.creator = creator
        self.description = description
        self.resources = resources or {}
        self.users = []  # added attribute for many-to-many relation

    def related_groups(self):
        # Your method implementation here
        pass


class Chat:
    def __init__(self):
        self.messages = []  # added attribute for one-to-many relation

    def add_message(self, message):
        self.messages.append(message)
        
        
        
class Group:
    GROUP_TYPE_CHOICES = ['study', 'project']

    def __init__(self, name, group_type, picture=None, description='', social_networks_links=None, creator=None):
        self.name = name
        self.group_type = group_type
        self.picture = picture
        self.description = description
        self.social_networks_links = social_networks_links or {}
        self.creator = creator
        self.members = []
        self.coordinators = []
        self.users_requests = []
        self.chat = Chat()

    def suggest_users(self):
        # Your method implementation here
        pass

    def request_to_join(self, user):
        # Your method implementation here
        pass

    def answer_request(self, user, response):
        # Your method implementation here
        pass

    def publish(self, social_networks_id, material, publish_locally):
        # Your method implementation here
        pass


class StudyGroup(Group):
    def __init__(self, name, group_type, skill, level=None, resources=None, **kwargs):
        super().__init__(name, group_type, **kwargs)
        self.skill = skill
        self.level = level
        self.resources = resources or {}
        self.skill.groups.append(self)  # added attribute for many-to-many relation



class ProjectGroup(Group):
    def __init__(self, name, group_type, active_project=None, skills=None, users_to_skills=None, archived_projects=None, **kwargs):
        super().__init__(name, group_type, **kwargs)
        self.active_project = active_project
        self.skills = skills or []
        self.users_to_skills = users_to_skills or {}
        self.archived_projects = archived_projects or []
        for skill in self.skills:
            skill.groups.append(self)  # added attribute for many-to-many relation

    def new_project(self):
        # Your method implementation here
        pass

    def select_project(self, project):
        # Your method implementation here
        pass

    def transfer_project(self, project, other_group):
        # Your method implementation here
        pass


class Project:
    def __init__(self, name, description='', picture=None, tasks=None, stage='', links=None, resources=None,
                 open_positions=None, users_to_skills=None, creator=None):
        self.name = name
        self.description = description
        self.picture = picture
        self.tasks = tasks or {}
        self.stage = stage
        self.links = links or {}
        self.resources = resources or {}
        self.open_positions = open_positions or {}
        self.users_to_skills = users_to_skills or {}
        self.creator = creator

    def assign_task(self, task):
        # Your method implementation here
        pass

    def submit_task(self, task):
        # Your method implementation here
        pass

    def update_stage(self, new_stage):
        # Your method implementation here
        pass


class Message:
    def __init__(self, title, context=None, reactions=None, chat=None, creator=None):
        self.title = title
        self.context = context
        self.reactions = reactions or {}
        self.chat = chat
        self.creator = creator
        if chat:
            chat.add_message(self)  # added attribute for one-to-many relation

    def add_reaction(self, user, reaction):
        # Your method implementation here
        pass

    def modify_reaction(self, user, reaction):
        # Your method implementation here
        pass


class User:
    def __init__(self, username, email, password, picture=None, personal_data=None, public_links=None,
                 notifications=None, accountability=None, skills=None, skill_levels=None, settings=None):
        self.username = username
        self.email = email
        self.password = password
        self.picture = picture
        self.personal_data = personal_data or {}
        self.public_links = public_links or {}
        self.notifications = notifications or {}
        self.accountability = accountability or {}
        self.skills = skills or []
        self.skill_levels = skill_levels or {}
        self.settings = settings or {}
        self.groups = []  # added attribute for many-to-many relation
        self.groups_coordinated = []  # added attribute for many-to-many relation
        self.group_requested = []  # added attribute for many-to-many relation
        self.created_groups = []  # added attribute for many-to-many relation
        self.created_skills = []  # added attribute for many-to-many relation
        self.created_projects = []  # added attribute for many-to-many relation
        self.messages = []  # added attribute for one-to-many relation
        

    def validate_password(self, password):
        pass

    def search_for_group(self, query):
        # Your method implementation here
        pass

    def search_for_project(self, query):
        # Your method implementation here
        pass

    def create_group(self, group):
        # Your method implementation here
        pass

    def create_project(self, project):
        # Your method implementation here
        pass
