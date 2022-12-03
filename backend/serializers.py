from rest_framework import serializers

from backend.models import *


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("status", "id")


class RequestDetailSerializer(serializers.ModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = Request
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentDetailSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ScheduleDetailSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()
    student = StudentSerializer()

    class Meta:
        model = Schedule
        fields = '__all__'
