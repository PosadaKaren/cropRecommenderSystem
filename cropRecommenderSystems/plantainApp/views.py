import json
from django import http
from django.shortcuts import render
from django.views import View
from plantainApp.utils import concat, correlation,  todf, fromquerytocrop, fromjsontocrop, mean
from plantainApp.models import crops, User
from plantainApp.serializers import cropsSerializer, userSearializer
from plantainApp.utils import normalize
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class cropViewSet(viewsets.ModelViewSet):
    queryset = crops.objects.all()
    serializer_class = cropsSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSearializer  

class userCropsViewSet(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        userCrop = json.loads(request.body)
        userCrop = fromjsontocrop(userCrop)
        #userCrop = normalize(userCrop)
        cropslist = crops.objects.values()
        cropslist = fromquerytocrop(cropslist)
        document = userCrop.append(cropslist, ignore_index=True)
        document = normalize(document)
        print(document)
        pearson = correlation(document)
        print(pearson)
        similarity = mean(pearson) * 100
        print(similarity)
        return JsonResponse({'similarity' : similarity})