from django.db import models

# Create your models here.
class Student(models.Model):
    rollnumber=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobile=models.CharField(max_length=15,unique=True)
    email=models.EmailField(max_length=25,unique=True)
    city=models.CharField(max_length=50)
class Meta:
    db_table="studentdata"
        