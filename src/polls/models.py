from django.db import models
 
# Create your models here.  
class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
 
    def __str__(self):
        return "{0}: {1} {2}".format(self.username, self.firstname,self.lastname)  
