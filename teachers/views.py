from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Count
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
        students_count = students_under.aggregate(count=Count('student'))['count']
        students = [enrollment.student for enrollment in students_under]
        serialized_students = StudentSerializer(students, many=True)

        serialized_teacher = self.get_serializer(teacher)

        data = {
            'teacher': serialized_teacher.data,
            'total': students_count,
            'enrolled_students': serialized_students.data  
        }

        return Response(data, status=status.HTTP_200_OK)