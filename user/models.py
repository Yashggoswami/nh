from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='ppic.jpg',upload_to='ppic')
    city = models.CharField(max_length=20,null=True)
    country =models.CharField(max_length=20,null=True)
    college=models.CharField(max_length=20,null=True)
    dob=models.DateField(max_length=20,null=True)

    def __str__(self):

        return f'{self.user.username } profile'



