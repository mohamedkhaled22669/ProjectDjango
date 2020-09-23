from django.db import models

# Create your models here.

class Posts(models.Model):
    
    id = models.AutoField(primary_key= True)
    topic = models.CharField(max_length = 50)
    content = models.CharField(max_length = 50)
    # datetime = models.DateField()
    user = models.EmailField(max_length = 50)
    picture = models.FileField(upload_to = 'pictures',null = True,blank= True)
    
    
    class Meta:
        db_table = 'Posts'
    
