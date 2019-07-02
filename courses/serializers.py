from rest_framework import serializers
from .models import Courses
from user.serializers import UserSerializer
from django.contrib.auth.models import User

class CoursesSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required=False)
    created_by_id = serializers.IntegerField(write_only=True,required=False,allow_null=True)
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
            'created_by_id',
            'created_by'
        )

    def create(self, validated_data):
        created_by_id = validated_data.get("created_by_id")
        validated_data.pop("created_by_id",None)

        course = Courses.objects.create(**validated_data)

        #relate with user
        user = User.objects.filter(id=created_by_id).first()
        course.created_by = user
        course.save()

        return course





