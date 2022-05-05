from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

class Docunent(models.Model):
    NNI = models.CharField(max_length=70, blank=False, default='')
    Nom = models.CharField(max_length=200,blank=False, default='')
    Prenom = models.CharField(max_length=70, blank=False, default='')
    Sex = models.CharField(max_length=200,blank=False, default='')
    date_naiss = models.CharField(max_length=70, blank=False, default='')
    dateValidie = models.CharField(max_length=200,blank=False, default='')
    Pays = models.CharField(max_length=70, blank=False, default='')
    typeDocument = models.CharField(max_length=200,blank=False, default='')
    NumeroDocument = models.CharField(max_length=70, blank=False, default='')
    Path = models.CharField(max_length=200,blank=False, default='')
