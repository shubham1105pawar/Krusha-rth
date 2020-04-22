from django.db import models
from django.utils import timezone as t
# Create your models here.

from django.contrib.auth.models import User,auth


class Crops(models.Model):
    name = models.CharField(max_length=50,unique=True)  
    image = models.ImageField(upload_to='pics')
    Description=models.TextField()
    def __str__(self):
        return self.name

#User._meta.get_field('email')._unique = True
 
class Diseases(models.Model):
    Disease_Name = models.CharField(max_length=50,unique=True)
    Disease_image = models.ImageField(upload_to='pics')
    Disease_Symptoms=models.TextField()
    Disease_Cause = models.CharField(max_length=30)
    Disease_Management = models.TextField()
    Crop = models.ForeignKey(Crops,to_field='name',on_delete=models.CASCADE)
     
    def __str__(self):
        return self.Disease_Name
 
class Pesticides(models.Model):
    Pesticide_Name = models.CharField(max_length=50,unique=True)
    Pesticide_image = models.ImageField(upload_to='pics')
    Pesticide_Price=models.FloatField()
    Pesticide_Quantity = models.CharField(max_length=7)
    Pesticide_Detail=models.TextField() 
    
    def __str__(self):
        return self.Pesticide_Name 
    
class PesticideDisease(models.Model):
     
    Disease_name = models.ForeignKey(Diseases,to_field='Disease_Name',on_delete=models.CASCADE)
    Pesticide_name = models.ForeignKey(Pesticides,to_field='Pesticide_Name',on_delete=models.CASCADE)
    ide = models.AutoField(primary_key=True) 
    def __str__(self):
        return str(self.ide )
        

class Rating(models.Model):
   
    Down_vote = models.IntegerField(default=0)
    Up_vote = models.IntegerField(default=0)
    Email = models.EmailField()
    Pesticide = models.CharField(max_length=50)
    Disease = models.CharField(max_length=50)
    ide = models.AutoField(primary_key=True) 
    def __str__(self):
        return str(self.ide)
    
class Question(models.Model):
    
    CropName = models.CharField(max_length=50)
    Questions = models.TextField()
    image = models.FileField(blank=True,upload_to='pics')
    Email = models.EmailField()
    date = models.DateTimeField(default=t.now)
    def __str__(self):
        return str(self.CropName)

class Answers(models.Model):
    
    UserName = models.CharField(max_length=50)
    Answer = models.TextField()
    Qid = models.ForeignKey(Question,on_delete=models.CASCADE)
    Email = models.EmailField()
    date = models.DateTimeField(default=t.now)
    def __str__(self):
        return str(self.Qid)


          