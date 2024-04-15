from rest_framework import serializers
from students.models import Student
from subjects.models import Subject
from teachers.models import Teacher
from .models import Enrollment
from teachers.serializers import TeacherSerializer


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

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all()
        )
    teacher = serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all()
        )
    subject = SubjectDetailsField(
        queryset=Subject.objects.all(), many=True
        )

    class Meta:
        model = Enrollment
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        teacher_instance = Teacher.objects.get(id=representation['teacher'])
        representation['teacher'] = TeacherSerializer(teacher_instance).data

        student_id = representation['student']
        student = Student.objects.get(id=student_id)
        representation['student'] = {
            "id": student.id,
            "lastname": student.lastname,
            "firstname": student.firstname, 
            "course": student.course
        }

        return representation
    
   

    


