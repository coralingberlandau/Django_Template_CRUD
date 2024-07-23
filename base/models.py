from django.db import models


# Create your models here.
class Book(models.Model):
   bookName = models.CharField(max_length=50, null=True, blank=True)
   author = models.CharField(max_length=50,null=True,blank=True)
   year = models.IntegerField()
   createdTime = models.DateTimeField(auto_now_add=True)
   fields =['bookName','author','year']
  
   def __str__(self):
       return self.bookName 