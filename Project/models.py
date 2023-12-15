from django.db import models

# Create your models here.

class Project(models.Model):
    name=models.CharField( max_length=50)
    number=models.IntegerField()
    email=models.EmailField()
    born=models.DateField(auto_now_add=False)
    create=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    