from django.shortcuts import render
from rest_framework import viewsets
from Project.serializer import ProjectSerializer
from Project.models import Project
# Create your views here.

class ProjectView(viewsets.ModelViewSet):
    serializer_class=ProjectSerializer
    queryset= Project.objects.all()
    
