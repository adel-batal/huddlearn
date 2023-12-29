IMAGE_SIZE=(300,300)

# from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOrReadOnly, IsCoordinatorOrReadOnly, IsUserOrReadOnly
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
    StudyGroupMembershipSerializer, ProjectGroupMembershipSerializer, UserSerializer, SkillListSerializer

from django_filters.rest_framework import DjangoFilterBackend
from .filters import StudyGroupFilter, ProjectGroupFilter

from PIL import Image


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        super().perform_create(serializer)
        instance = serializer.instance

        if instance.picture is not None:
            try:
                original_image = Image.open(instance.picture.path)
                # Resize the image (adjust the size as needed)
                original_image.thumbnail(IMAGE_SIZE, Image.LANCZOS)
                # Save the resized image back to the same path
                original_image.save(instance.picture.path, format=original_image.format)
            except (FileNotFoundError, IOError, ValueError):
                instance.picture = None
                instance.save()

    def perform_update(self, serializer):
        # Handle the existing picture file
        old_instance = HuddleUser.objects.get(pk=serializer.instance.pk)
        old_picture = old_instance.picture

        # Call the serializer's update method to update the instance
        super().perform_update(serializer)

        # Handle the new picture file
        new_picture = serializer.instance.picture

        # Delete the old picture file if it has changed
        if old_picture and old_picture != new_picture:
            old_picture.delete(save=False)

        # Resize the new picture file
        if new_picture is not None:
            try:
                original_image = Image.open(new_picture.path)
                # Resize the image (adjust the size as needed)
                original_image.thumbnail(IMAGE_SIZE, Image.LANCZOS)
                # Save the resized image back to the same path
                original_image.save(new_picture.path, format=original_image.format)
            except (FileNotFoundError, IOError, ValueError):
                serializer.instance.picture = None
                serializer.instance.save()


    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly])
    def add_skill(self, request, pk=None):
        huddleuser = self.get_object()
        # request_huddleuser = HuddleUser.objects.get(user=self.request.user)
        serializer = SkillListSerializer(data=request.data)

        if serializer.is_valid():
            skill_id = serializer.validated_data['skill_id']
            try:
                skill = Skill.objects.get(pk=skill_id)
            except:
                return Response({'message': f'Skill ID {skill_id} don`t exist'},
                                status=status.HTTP_400_BAD_REQUEST)
            if huddleuser.skills.filter(id=skill.id).exists():
                return Response({'message': 'Skill already assigned to user'},
                                status=status.HTTP_400_BAD_REQUEST)

            # Add the user to the group's members
            huddleuser.skills.add(skill)
            huddleuser.save()
            return Response({'message': 'Skill added to user successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly])
    def remove_skill(self, request, pk=None):
        huddleuser = self.get_object()
        # request_huddleuser = HuddleUser.objects.get(user=self.request.user)
        serializer = SkillListSerializer(data=request.data)

        if serializer.is_valid():
            skill_id = serializer.validated_data['skill_id']
            try:
                skill = Skill.objects.get(pk=skill_id)
            except:
                return Response({'message': f'Skill ID {skill_id} don`t exist'},
                                status=status.HTTP_400_BAD_REQUEST)
            if not huddleuser.skills.filter(id=skill.id).exists():
                return Response({'message': 'Skill cannot be removed, because it is not assigned to user'},
                                status=status.HTTP_400_BAD_REQUEST)
            huddleuser.skills.remove(skill)
            huddleuser.save()
            return Response({'message': 'Skill removed from user successfully'}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

        super().perform_create(serializer)
        instance = serializer.instance

        if instance.picture is not None:
            try:
                original_image = Image.open(instance.picture.path)
                # Resize the image (adjust the size as needed)
                original_image.thumbnail(IMAGE_SIZE, Image.LANCZOS)
                # Save the resized image back to the same path
                original_image.save(instance.picture.path, format=original_image.format)
            except (FileNotFoundError, IOError, ValueError):
                instance.picture = None
                instance.save()


    def perform_update(self, serializer):
        # Handle the existing picture file
        old_instance = Skill.objects.get(pk=serializer.instance.pk)
        old_picture = old_instance.picture

        # Call the serializer's update method to update the instance
        super().perform_update(serializer)

        # Handle the new picture file
        new_picture = serializer.instance.picture

        # Delete the old picture file if it has changed
        if old_picture and old_picture != new_picture:
            old_picture.delete(save=False)

        # Resize the new picture file
        if new_picture is not None:
            try:
                original_image = Image.open(new_picture.path)
                # Resize the image (adjust the size as needed)
                original_image.thumbnail(IMAGE_SIZE, Image.LANCZOS)
                # Save the resized image back to the same path
                original_image.save(new_picture.path, format=original_image.format)
            except (FileNotFoundError, IOError, ValueError):
                serializer.instance.picture = None
                serializer.instance.save()

class StudyGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # authentication_classes = [JWTAuthentication]

    queryset = StudyGroup.objects.all().order_by('name')
    serializer_class = StudyGroupSerializer
    permission_classes = [permissions.IsAuthenticated, IsCoordinatorOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_class = StudyGroupFilter

    @transaction.atomic
    def perform_create(self, serializer):
        creator_default_value = HuddleUser.objects.get(user=self.request.user)

        serializer.validated_data['creator'] = creator_default_value
        # Save the instance
        super().perform_create(serializer)
        instance = serializer.instance
        # Add the creator to the list of members and coordinators
        instance.members.add(creator_default_value)
        instance.coordinators.add(creator_default_value)
        group_chat = Chat.objects.create()
        instance.chat = group_chat
        instance.save()
        if instance.picture is not None:
            try:
                original_image = Image.open(instance.picture.path)
                # Resize the image (adjust the size as needed)
                original_image.thumbnail(IMAGE_SIZE, Image.LANCZOS)
                # Save the resized image back to the same path
                original_image.save(instance.picture.path, format=original_image.format)
            except (FileNotFoundError, IOError, ValueError):
                instance.picture = None
                instance.save()

        # serializer.save(creator=self.request.user)
    def perform_update(self, serializer):
        # Handle the existing picture file
        old_instance = StudyGroup.objects.get(pk=serializer.instance.pk)
        old_picture = old_instance.picture

        # Call the serializer's update method to update the instance
        super().perform_update(serializer)

        # Handle the new picture file
        new_picture = serializer.instance.picture

        # Delete the old picture file if it has changed
        if old_picture and old_picture != new_picture:
            old_picture.delete(save=False)

        # Resize the new picture file
        if new_picture is not None:
            try:
                original_image = Image.open(new_picture.path)
                # Resize the image (adjust the size as needed)
                original_image.thumbnail(IMAGE_SIZE, Image.LANCZOS)
                # Save the resized image back to the same path
                original_image.save(new_picture.path, format=original_image.format)
            except (FileNotFoundError, IOError, ValueError):
                serializer.instance.picture = None
                serializer.instance.save()



    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def add_member(self, request, pk=None):
        group = self.get_object()
        request_huddleuser = HuddleUser.objects.get(user=self.request.user)
        serializer = StudyGroupMembershipSerializer(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            try:
                user_to_add = HuddleUser.objects.get(pk=user_id)
            except:
                return Response({'message': f'Huddleuser with ID {user_id} don`t exist'},
                                status=status.HTTP_400_BAD_REQUEST)
            if group.members.filter(id=user_to_add.id).exists():
                return Response({'message': 'User allready a member of the group'},
                                status=status.HTTP_400_BAD_REQUEST)
            if (group.creator == request_huddleuser) or (
                    group.coordinators.filter(id=request_huddleuser.id).exists()):
                # Add the user to the group's members
                group.members.add(user_to_add)
                group.save()
                return Response({'message': 'User added to group successfully'}, status=status.HTTP_201_CREATED)
            else:
                if group.users_requests.filter(id=user_to_add.id).exists():
                    return Response(
                        {'message': 'You can only add user to request list, but this user is already in it'},
                        status=status.HTTP_400_BAD_REQUEST)
                group.users_requests.add(user_to_add)
                group.save()
                return Response({'message':
                                     'You can only add user to request list, User was added to request list successfully'},
                                status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def remove_member(self, request, pk=None):
        group = self.get_object()
        request_huddleuser = HuddleUser.objects.get(user=self.request.user)
        serializer = StudyGroupMembershipSerializer(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            try:
                user_to_del = HuddleUser.objects.get(pk=user_id)
            except:
                return Response({'message': f'Huddleuser with ID {user_id} don`t exist'},
                                status=status.HTTP_400_BAD_REQUEST)
            if (user_to_del == group.creator):
                return Response({'message': 'Group creator cannot be removed from group'},
                                status=status.HTTP_400_BAD_REQUEST)
            if (user_to_del == request_huddleuser) or \
                    (group.creator == request_huddleuser) or \
                    (group.coordinators.filter(id=request_huddleuser.id).exists()):
                if group.members.filter(id=user_to_del.id).exists():
                    # Remove the user from the group's members
                    group.members.remove(user_to_del)
                    if group.coordinators.filter(id=user_to_del.id).exists():
                        group.coordinators.remove(user_to_del)

                    group.save()

                    return Response({'message': 'User removed from group successfully'}, status=status.HTTP_200_OK)
                else:
                    if group.users_requests.filter(id=user_to_del.id).exists():
                        group.users_requests.remove(user_to_del)
                        group.save()
                        return Response(
                            {'message': 'User was in the request list, and was removed from it'},
                            status=status.HTTP_200_OK)
                    return Response({'message': 'User is not a member of the group'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'You don`t have required permissions'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'],
            permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsCoordinatorOrReadOnly])
    def add_skill(self, request, pk=None):
        group = self.get_object()
        # request_huddlexuser = HuddleUser.objects.get(user=self.request.user)
        serializer = SkillListSerializer(data=request.data)

        if serializer.is_valid():
            skill_id = serializer.validated_data['skill_id']
            try:
                skill = Skill.objects.get(pk=skill_id)
            except:
                return Response({'message': f'Skill ID {skill_id} don`t exist'},
                                status=status.HTTP_400_BAD_REQUEST)
            if group.skills.filter(id=skill.id).exists():
                return Response({'message': 'Skill already assigned to group'},
                                status=status.HTTP_400_BAD_REQUEST)

            # Add the user to the group's members
            group.skills.add(skill)
            group.save()
            return Response({'message': 'Skill added to group successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'],
            permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsCoordinatorOrReadOnly])
    def remove_skill(self, request, pk=None):
        group = self.get_object()
        # request_huddleuser = HuddleUser.objects.get(user=self.request.user)
        serializer = SkillListSerializer(data=request.data)

        if serializer.is_valid():
            skill_id = serializer.validated_data['skill_id']
            try:
                skill = Skill.objects.get(pk=skill_id)
            except:
                return Response({'message': f'Skill ID {skill_id} don`t exist'},
                                status=status.HTTP_400_BAD_REQUEST)
            if not group.skills.filter(id=skill.id).exists():
                return Response({'message': 'Skill cannot be removed, because it is not assigned to group'},
                                status=status.HTTP_400_BAD_REQUEST)
            group.skills.remove(skill)
            group.save()
            return Response({'message': 'Skill removed from group successfully'}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ProjectGroup.objects.all().order_by('name')
    serializer_class = ProjectGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectGroupFilter

    @transaction.atomic
    def perform_create(self, serializer):
        creator_default_value = HuddleUser.objects.get(user=self.request.user)

        serializer.validated_data['creator'] = creator_default_value
        # Save the instance
        super().perform_create(serializer)
        instance = serializer.instance
        # Add the creator to the list of members and coordinators
        instance.members.add(creator_default_value)
        instance.coordinators.add(creator_default_value)
        group_chat = Chat.objects.create()
        instance.chat = group_chat
        instance.save()
        if instance.picture is not None:
            try:
                original_image = Image.open(instance.picture.path)
                # Resize the image (adjust the size as needed)
                original_image.thumbnail(IMAGE_SIZE, Image.LANCZOS)
                # Save the resized image back to the same path
                original_image.save(instance.picture.path, format=original_image.format)
            except (FileNotFoundError, IOError, ValueError):
                instance.picture = None
                instance.save()

    def perform_update(self, serializer):
        # Handle the existing picture file
        old_instance = ProjectGroup.objects.get(pk=serializer.instance.pk)
        old_picture = old_instance.picture

        # Call the serializer's update method to update the instance
        super().perform_update(serializer)

        # Handle the new picture file
        new_picture = serializer.instance.picture

        # Delete the old picture file if it has changed
        if old_picture and old_picture != new_picture:
            old_picture.delete(save=False)

        # Resize the new picture file
        if new_picture is not None:
            try:
                original_image = Image.open(new_picture.path)
                # Resize the image (adjust the size as needed)
                original_image.thumbnail(IMAGE_SIZE, Image.LANCZOS)
                # Save the resized image back to the same path
                original_image.save(new_picture.path, format=original_image.format)
            except (FileNotFoundError, IOError, ValueError):
                serializer.instance.picture = None
                serializer.instance.save()


    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def add_member(self, request, pk=None):
        group = self.get_object()
        request_huddleuser = HuddleUser.objects.get(user=self.request.user)
        serializer = ProjectGroupMembershipSerializer(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            try:
                user_to_add = HuddleUser.objects.get(pk=user_id)
            except:
                return Response({'message': f'Huddleuser with ID {user_id} don`t exist'},
                                status=status.HTTP_400_BAD_REQUEST)
            if group.members.filter(id=user_to_add.id).exists():
                return Response({'message': 'User allready a member of the group'},
                                status=status.HTTP_400_BAD_REQUEST)
            if (group.creator == request_huddleuser) or (
                    group.coordinators.filter(id=request_huddleuser.id).exists()):
                # Add the user to the group's members
                group.members.add(user_to_add)
                group.save()
                return Response({'message': 'User added to group successfully'}, status=status.HTTP_201_CREATED)
            else:
                if group.users_requests.filter(id=user_to_add.id).exists():
                    return Response(
                        {'message': 'You can only add user to request list, but this user is already in it'},
                        status=status.HTTP_400_BAD_REQUEST)
                group.users_requests.add(user_to_add)
                group.save()
                return Response({'message':
                                     'You can only add user to request list, User was added to request list successfully'},
                                status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def remove_member(self, request, pk=None):
        group = self.get_object()
        request_huddleuser = HuddleUser.objects.get(user=self.request.user)
        serializer = ProjectGroupMembershipSerializer(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            try:
                user_to_del = HuddleUser.objects.get(pk=user_id)
            except:
                return Response({'message': f'Huddleuser with ID {user_id} don`t exist'},
                                status=status.HTTP_400_BAD_REQUEST)
            if (user_to_del == group.creator):
                return Response({'message': 'Group creator cannot be removed from group'},
                                status=status.HTTP_400_BAD_REQUEST)
            if (user_to_del == request_huddleuser) or \
                    (group.creator == request_huddleuser) or \
                    (group.coordinators.filter(id=request_huddleuser.id).exists()):
                if group.members.filter(id=user_to_del.id).exists():
                    # Remove the user from the group's members
                    group.members.remove(user_to_del)
                    if group.coordinators.filter(id=user_to_del.id).exists():
                        group.coordinators.remove(user_to_del)

                    group.save()

                    return Response({'message': 'User removed from group successfully'}, status=status.HTTP_200_OK)
                else:
                    if group.users_requests.filter(id=user_to_del.id).exists():
                        group.users_requests.remove(user_to_del)
                        group.save()
                        return Response(
                            {'message': 'User was in the request list, and was removed from it'},
                            status=status.HTTP_200_OK)
                    return Response({'message': 'User is not a member of the group'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'You don`t have required permissions'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'],
            permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsCoordinatorOrReadOnly])
    def add_skill(self, request, pk=None):
        group = self.get_object()
        # request_huddlexuser = HuddleUser.objects.get(user=self.request.user)
        serializer = SkillListSerializer(data=request.data)

        if serializer.is_valid():
            skill_id = serializer.validated_data['skill_id']
            try:
                skill = Skill.objects.get(pk=skill_id)
            except:
                return Response({'message': f'Skill ID {skill_id} don`t exist'},
                                status=status.HTTP_400_BAD_REQUEST)
            if group.skills.filter(id=skill.id).exists():
                return Response({'message': 'Skill already assigned to group'},
                                status=status.HTTP_400_BAD_REQUEST)

            # Add the user to the group's members
            group.skills.add(skill)
            group.save()
            return Response({'message': 'Skill added to group successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'],
            permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsCoordinatorOrReadOnly])
    def remove_skill(self, request, pk=None):
        group = self.get_object()
        # request_huddleuser = HuddleUser.objects.get(user=self.request.user)
        serializer = SkillListSerializer(data=request.data)

        if serializer.is_valid():
            skill_id = serializer.validated_data['skill_id']
            try:
                skill = Skill.objects.get(pk=skill_id)
            except:
                return Response({'message': f'Skill ID {skill_id} don`t exist'},
                                status=status.HTTP_400_BAD_REQUEST)
            if not group.skills.filter(id=skill.id).exists():
                return Response({'message': 'Skill cannot be removed, because it is not assigned to group'},
                                status=status.HTTP_400_BAD_REQUEST)
            group.skills.remove(skill)
            group.save()
            return Response({'message': 'Skill removed from group successfully'}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
