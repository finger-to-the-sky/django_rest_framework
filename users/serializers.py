from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, StringRelatedField
from .models import User, Project, ToDo


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = ('name', 'url', 'created_at', 'users')


class ToDoModelSerializer(ModelSerializer):
    user = StringRelatedField()
    project = StringRelatedField()

    class Meta:
        model = ToDo
        exclude = ('id', )