# filters.py
import django_filters
from .models import StudyGroup, Skill, ProjectGroup


class StudyGroupFilter(django_filters.FilterSet):
    skills = django_filters.ModelMultipleChoiceFilter(
        field_name='skills__id',
        queryset=Skill.objects.all(),
        to_field_name='id',
        conjoined=True
    )

    class Meta:
        model = StudyGroup
        fields = ['skills']


class ProjectGroupFilter(django_filters.FilterSet):
    skills = django_filters.ModelMultipleChoiceFilter(
        field_name='skills__id',
        queryset=Skill.objects.all(),
        to_field_name='id',
        conjoined=True
    )

    class Meta:
        model = ProjectGroup
        fields = ['skills']
