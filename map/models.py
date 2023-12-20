from django.db import models

# Create your models here.

class Configh(models.Model):
    titleFontSize   = models.CharField(max_length = 20 ,default = 12)
    titleFontColor  = models.CharField(max_length = 20 ,default = '#000')
    bodyFontColor   = models.CharField(max_length = 20 ,default = '#000')
    backgroundColor = models.CharField(max_length = 20 ,default = '#fff')
    cornerRadius    = models.CharField(max_length = 20 ,default = 3)
    position        = models.CharField(max_length = 20 ,default = 'top')
   

    
