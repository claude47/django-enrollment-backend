from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Subject
from .serializers import SubjectSerializer
from enrollment.models import Enrollment
from students.serializers import StudentSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def retrieve(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        enrolled_students = Enrollment.objects.filter(subject=subject)
        students = [enrollment.student for enrollment in enrolled_students]
        serialized_students = StudentSerializer(students, many=True)
        serialized_subject = self.get_serializer(subject)

        data = {
            'subject': serialized_subject.data,
            'enrolled_students': serialized_students.data
        }

        return Response(data, status=status.HTTP_200_OK)
