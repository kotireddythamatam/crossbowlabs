from django.db import models

# Create your models here.
class Student_model(models.Model):
    name = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='pic_folder/')
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    password = models.CharField(max_length=10)
    conform_password = models.CharField(max_length=10)
    def __str__(self):
        return self.name
