# from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOrReadOnly, IsCoordinatorOrReadOnly
from rest_framework import generics
from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from django.db import transaction

from .models import HuddleUser, Skill, StudyGroup, ProjectGroup, Chat
from .serializers import HuddleUserSerializer, StudyGroupSerializer, ProjectGroupSerializer, SkillSerializer, \
    StudyGroupMembershipSerializer, ProjectGroupMembershipSerializer, UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create the user with a hashed password
        user_data = serializer.validated_data
        user_data['password'] = make_password(user_data['password'])
        user = User.objects.create(**user_data)

        # Create a corresponding HuddleUser instance
        HuddleUser.objects.create(user=user, fullname=user_data['username'])

        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response(data, status=status.HTTP_201_CREATED)


class HuddleUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = HuddleUser.objects.all().order_by('user__date_joined')
    serializer_class = HuddleUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Skill.objects.all().order_by('name')
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        creator_default_value = HuddleUser.objects.get(user=self.request.user)

        serializer.validated_data['creator'] = creator_default_value

        instance = serializer.save()


class StudyGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # authentication_classes = [JWTAuthentication]

    queryset = StudyGroup.objects.all().order_by('name')
    serializer_class = StudyGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def perform_create(self, serializer):
        creator_default_value = HuddleUser.objects.get(user=self.request.user)

        serializer.validated_data['creator'] = creator_default_value
        # Save the instance
        instance = serializer.save()
        # Add the creator to the list of members and coordinators
        instance.members.add(creator_default_value)
        instance.coordinators.add(creator_default_value)
        group_chat=Chat.objects.create()
        instance.chat=group_chat
        instance.save()


        # serializer.save(creator=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsCoordinatorOrReadOnly])
    def add_member(self, request, pk=None):
        group = self.get_object()
        serializer = StudyGroupMembershipSerializer(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            user = HuddleUser.objects.get(pk=user_id)

            # Add the user to the group's members
            group.members.add(user)
            group.save()

            return Response({'message': 'User added to group successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsCoordinatorOrReadOnly])
    def remove_member(self, request, pk=None):
        group = self.get_object()
        serializer = StudyGroupMembershipSerializer(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            user = HuddleUser.objects.get(pk=user_id)

            # Remove the user from the group's members
            group.members.remove(user)
            group.save()

            return Response({'message': 'User removed from group successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ProjectGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProjectGroup.objects.all().order_by('name')
    serializer_class = ProjectGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @transaction.atomic
    def perform_create(self, serializer):
        creator_default_value = HuddleUser.objects.get(user=self.request.user)

        serializer.validated_data['creator'] = creator_default_value
        # Save the instance
        instance = serializer.save()
        # Add the creator to the list of members and coordinators
        instance.members.add(creator_default_value)
        instance.coordinators.add(creator_default_value)
        group_chat=Chat.objects.create()
        instance.chat=group_chat
        instance.save()


    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsCoordinatorOrReadOnly])
    def add_member(self, request, pk=None):
        group = self.get_object()
        serializer = ProjectGroupMembershipSerializer(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            user = HuddleUser.objects.get(pk=user_id)

            # Add the user to the group's members
            group.members.add(user)
            group.save()

            return Response({'message': 'User added to group successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsCoordinatorOrReadOnly])
    def remove_member(self, request, pk=None):
        group = self.get_object()
        serializer = ProjectGroupMembershipSerializer(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            user = HuddleUser.objects.get(pk=user_id)

            # Remove the user from the group's members
            group.members.remove(user)
            group.save()

            return Response({'message': 'User removed from group successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


