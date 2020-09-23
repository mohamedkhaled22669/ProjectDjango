from django.db import models

# Create your models here.

class Member(models.Model):

    
    username = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50, primary_key = True)
    password = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'Member'
    

