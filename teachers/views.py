from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer
from enrollment.models import Enrollment
from students.serializers import StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def retrieve(self, request, pk=None):
        teacher = get_object_or_404(Teacher, pk=pk)
        students_under = Enrollment.objects.filter(teacher=teacher)
        students = [enrollment.student for enrollment in students_under]
        serialized_students = StudentSerializer(students, many=True)
        serialized_teacher = self.get_serializer(teacher)

        data = {
            'teacher': serialized_teacher.data,
            'enrolled_students': serialized_students.data  # Access serialized data
        }

        return Response(data, status=status.HTTP_200_OK)