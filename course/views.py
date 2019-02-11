from django.shortcuts import render
from rest_framework.views import APIView
from .models import Course
from .serializers import GetAllCourseSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class GetAllCouse(APIView):

    def get(self, request):
        data1 = Course.objects.all()
        mydata = GetAllCourseSerializer(data1, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

