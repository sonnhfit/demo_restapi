from rest_framework import serializers
from .models import Course


class GetAllCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title')


class KeySerializer(serializers.Serializer):
    key_price = serializers.CharField(max_length=50, required=True)
