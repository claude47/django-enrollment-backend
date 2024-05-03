from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Teacher
from .serializers import TeacherSerializer
from enrollment.models import Enrollment
from students.serializers import StudentSerializer

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3

class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    pagination_class = CustomPageNumberPagination 

    def get_queryset(self):
        return Teacher.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
