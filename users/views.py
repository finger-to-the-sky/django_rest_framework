from rest_framework.viewsets import ModelViewSet
from .models import User, Project, ToDo
from .serializers import UserModelSerializer, ProjectModelSerializer, ToDoModelSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoView(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
