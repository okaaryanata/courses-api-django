from rest_framework import serializers
from .models import Courses
from user.serializers import UserSerializer
from curriculums.serializers import CurriculumsSerializer,CurriculumsSerializerSimple
from django.contrib.auth.models import User

class CoursesSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required=False)
    curriculums = CurriculumsSerializerSimple(many=True,read_only=True)
    class Meta:
        model = Courses
        fields = (
            'id',
            'title',
            'subtitle',
            'description',
            'video_url',
            'price',
            'image_url',
            'created_by',
            'curriculums'
        )

    def create(self, validated_data):

        course = Courses.objects.create(**validated_data)
        course.save()

        return course

class CoursesSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'id',
            'title',
            'subtitle',
            'description',
            'video_url',
            'price',
            'image_url',
        )




