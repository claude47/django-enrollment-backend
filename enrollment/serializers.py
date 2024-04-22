from rest_framework import serializers
from students.models import Student
from subjects.models import Subject
from teachers.models import Teacher
from .models import Enrollment
from teachers.serializers import TeacherSerializer


class SubjectDetailsField(serializers.RelatedField):
    def to_representation(self, value):
        return {
            "id": value.id,
            "uuid": value.uuid,
            "code": value.code,
            "title": value.title,
            "description": value.description
        }

    def to_internal_value(self, data):
        return data

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    subject = SubjectDetailsField(queryset=Subject.objects.all(), many=True)

    class Meta:
        model = Enrollment
        fields = ('id', 'uuid', 'enrollment_id', 
                  'enrollment_date', 'student', 'teacher', 'subject')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        teacher_instance = Teacher.objects.get(id=representation['teacher'])
        representation['teacher'] = TeacherSerializer(teacher_instance).data

        student_id = representation['student']
        student = Student.objects.get(id=student_id)
        representation['student'] = {
            "id": student.id,
            "uuid": student.uuid,
            "student_id": student.student_id,
            "lastname": student.lastname,
            "firstname": student.firstname, 
            "gender": student.gender,
            "course": student.course
        }

        return representation
    
    def validate(self, data):
        student = data['student']
        subjects = data['subject']
        for subject in subjects:
            if Enrollment.objects.filter(student=student, subject=subject).exists():
                    raise serializers.ValidationError("This student is already enrolled in one of the subjects.")
        
        teacher = data['teacher']
        if Enrollment.objects.filter(student=student, teacher=teacher).exists():
            raise serializers.ValidationError("This student is already enrolled with this teacher.")

        return data
    
   

    


