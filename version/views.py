from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from .models import AppVersion
from .serializers import AppVersionSerializer


class AppVersionList(generics.ListAPIView):
	"""
	Get API for the App Version
	"""
	queryset = AppVersion.objects.all()
	serializer_class = AppVersionSerializer
    
class AppVersionCreate(generics.CreateAPIView):
	"""
	Create API for the App Version
	"""
	qs = AppVersion.objects.all()
	serializer_class = AppVersionSerializer


class AppVersionDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	PUT & DELETE API for the App Version
	"""
	queryset = AppVersion.objects.all()
	serializer_class = AppVersionSerializer