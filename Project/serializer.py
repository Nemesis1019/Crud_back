from rest_framework import serializers
from Project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'