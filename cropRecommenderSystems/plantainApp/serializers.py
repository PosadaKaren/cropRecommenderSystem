
from dataclasses import fields
from plantainApp.models import crops, userCrops, User
from rest_framework import serializers

class cropsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = crops
        fields = ['fosforo', 'aluminio', 'calcio', 'potasio', 'sodio', 'zinc', 'pearson']


class userCropsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = userCrops
        fields = ['fosforo', 'aluminio', 'calcio', 'potasio', 'sodio', 'zinc', 'pearson', 'isUsefulForPlantain']

class userSearializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'password']