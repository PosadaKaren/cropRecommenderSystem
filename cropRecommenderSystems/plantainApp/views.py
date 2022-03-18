import json
from django import http
from django.shortcuts import render
from django.views import View
from plantainApp.utils import concat, correlation,  todf, fromquerytocrop, fromjsontocrop, mean, type, maxelements, datatolist
from plantainApp.models import crops, User, PlantainTypes
from plantainApp.serializers import cropsSerializer, userSearializer, PlantainTypeSerializer
from plantainApp.utils import normalize
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

class cropViewSet(viewsets.ModelViewSet):
    queryset = crops.objects.all()
    serializer_class = cropsSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSearializer  

class plantainViewSet(viewsets.ModelViewSet):
    queryset = PlantainTypes.objects.all()
    serializer_class = PlantainTypeSerializer 

class userCropsViewSet(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        userCrop = json.loads(request.body)
        userCrop = fromjsontocrop(userCrop)

        cropslist = crops.objects.values()
        cropslist = fromquerytocrop(cropslist)
        document = userCrop.append(cropslist, ignore_index=True)

        pearson = correlation(document, 3)
        
        top = maxelements(pearson,5)
        similarity = mean(pearson) * 100

        documentp = pd.DataFrame()
        documentp = document
        documentp['pearson'] = pearson2 = correlation(document, 3)
    
        docmax = pd.DataFrame()
        docmax = documentp
        docmax = (documentp[documentp.pearson >= min(top)])

        doctypes = type(userCrop)
        print(doctypes)
        

        return JsonResponse({'similarity' : similarity, 'pearson' : pearson2, 'type' : doctypes, 'document' : docmax.values.tolist() })