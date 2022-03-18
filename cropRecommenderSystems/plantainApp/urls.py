from django import views
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from plantainApp.views import cropViewSet, userCropsViewSet, plantainViewSet


router = routers.DefaultRouter()
router.register(r'crops', cropViewSet)
router.register(r'plantain', plantainViewSet )

urlpatterns = [
    path('', include(router.urls)),
    path('usercrops', userCropsViewSet.as_view(), name="useradd")
]