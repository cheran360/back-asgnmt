from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
# Create your views here.

@api_view(['POST'])
def createRecord(request):
    data = request.data
    try:
        record = Record.objects.create(
            name=data.get('name'),
            species=data.get('species'),
            weight=data.get('weight'),
            length=data.get('length'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
        )

        record.save()
        return Response({"message":"record added successfully"}, status=status.HTTP_201_CREATED)
    except:
        return Response({"message":"error in record u added"}, status=status.HTTP_400_BAD_REQUEST)

