from django.db import models

# Create your models here.

class data(models.Model):
    q1=models.TextField(max_length=50)
    q2=models.TextField(max_length=50)
    q3=models.CharField(max_length=50)
    q4=models.CharField(max_length=50)
    q5=models.CharField(max_length=50)

    def __str__(self):
        return self.q1

