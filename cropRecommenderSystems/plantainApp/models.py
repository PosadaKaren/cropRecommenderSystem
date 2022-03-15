from django.db import models

class crops(models.Model):
   fosforo = models.FloatField(max_length=10)
   aluminio = models.FloatField(max_length=10)
   calcio = models.FloatField(max_length=10)
   potasio = models.FloatField(max_length=10)
   sodio = models.FloatField(max_length=10)
   zinc = models.FloatField(max_length=10)
   pearson = models.FloatField(max_length=10)

class User(models.Model):
   user_id = models.AutoField(primary_key=True)
   usuario = models.TextField(max_length=20)
   contraseña = models.TextField(max_length=20)


class userCrops(models.Model):
   userCrop_id = models.AutoField(primary_key=True)
   fosforo = models.FloatField(max_length=10)
   aluminio = models.FloatField(max_length=10)
   calcio = models.FloatField(max_length=10)
   potasio = models.FloatField(max_length=10)
   sodio = models.FloatField(max_length=10)
   zinc = models.FloatField(max_length=10)
   pearson = models.FloatField(max_length=10)
   isUsefulForPlantain = models.FloatField(max_length=10, blank=True)
   user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

