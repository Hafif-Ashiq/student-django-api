import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)


    class Meta:
        abstract = True


class Student(BaseModel):
    name = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images',default='none')


