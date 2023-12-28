from django.contrib.auth.models import User
from rest_framework import serializers


from .models import Skill, StudyGroup,ProjectGroup,Project,Message,HuddleUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class HuddleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuddleUser
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    # creator=serializers.HyperlinkedIdentityField(view_name='HuddleUserViewSet', format='html', read_only=True)
    class Meta:
        model = Skill
        fields = '__all__'


class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = '__all__'
        extra_kwargs = {
            'members': {'required': False},
            'coordinators': {'required': False},
            'users_requests': {'required': False},
            'chat':{'required': False}
        }

class StudyGroupMembershipSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()  # Assuming user_id is sent in the request



class ProjectGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGroup
        fields = '__all__'
        extra_kwargs = {
            'members': {'required': False},
            'coordinators': {'required': False},
            'users_requests': {'required': False},
            'skills':{'required': False},
            'chat':{'required': False},
            'archived_projects':{'required': False},
        }

class ProjectGroupMembershipSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()  # Assuming user_id is sent in the request



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

#
# class ChatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Chat
#         fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'