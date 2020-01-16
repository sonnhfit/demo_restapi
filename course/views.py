from django.shortcuts import render
from rest_framework.views import APIView
from .models import Course, KeyCode
from .serializers import GetAllCourseSerializer, KeySerializer
from rest_framework.response import Response
from django.http import HttpResponse
from django.views import View
from rest_framework import status
# Create your views here.


class GetAllCouse(APIView):

    def get(self, request):
        data1 = Course.objects.all()
        mydata = GetAllCourseSerializer(data1, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

    def post(self, request):
        validate = KeySerializer(data=request.data)

        if not validate.is_valid():
            return Response('may gui sai du lieu roi', status=status.HTTP_400_BAD_REQUEST)

        mykey = validate.data['key_price']
        KeyCode.objects.create(key=mykey)

        return Response('them thanh cong', status=status.HTTP_200_OK)


def index(request):
    return HttpResponse('xin chao day la function base view ')


class Home(View):
    def get(self, request):
        return HttpResponse('xin chao day la class base view')
