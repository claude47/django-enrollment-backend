from rest_framework import serializers
from students.models import Student
from subjects.models import Subject
from .models import Enrollment
from subjects.serializers import SubjectSerializer


class SubjectDetailsField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "subject_id": value.id,
            "code": value.code,
            "title": value.title,
            "description": value.description
        }

    def to_internal_value(self, data):
        return data
    

class StudentDetailsField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "student_id": value.id,
            "lastname": value.lastname,
            "firstname": value.firstname
        }
    
    def to_internal_value(self, data):
        return data


class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentDetailsField(queryset=Student.objects.all())
    subject = SubjectDetailsField(queryset=Subject.objects.all(), many=True)

    class Meta:
        model = Enrollment
        fields = '__all__'


