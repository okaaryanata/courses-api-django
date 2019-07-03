from rest_framework import serializers
from .models import Curriculums
from user.serializers import UserSerializer
from rest_framework_recursive.fields import RecursiveField
from courses.models import Courses
from .constants import *

class CurriculumsSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required=False)
    course = RecursiveField('courses.serializers.CoursesSerializerSimple')
    course_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    class Meta:
        model = Curriculums
        fields = (
            'id',
            'title',
            'attachment_url',
            'type',
            'created_by_id',
            'created_by',
            'course',
            'course_id'
        )

    def create(self, validated_data):

        curriculum = Curriculums.objects.create(**validated_data)

        # relate with course
        course_id = validated_data.get("course_id")
        validated_data.pop("course_id", None)
        course = Courses.objects.filter(id=course_id).first()
        curriculum.course = course
        if validated_data.get("type") == "1":
            curriculum.type = TYPE_VIDEO
        elif validated_data.get("type") == "2":
            curriculum.type = TYPE_TEXT
        elif validated_data.get("type") == "3":
            curriculum.type = TYPE_VOICE
        curriculum.save()

        return curriculum

class CurriculumsSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Curriculums
        fields = (
            'id',
            'title',
            'attachment_url',
            'type'
        )



