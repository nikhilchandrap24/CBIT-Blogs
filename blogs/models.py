from django.db import models
from django.db.models.fields import DateField
from django.contrib.auth.models import User
from datetime import datetime

class BlogData(models.Model):
    title = models.CharField(max_length=150)
    student = models.ForeignKey(User,on_delete=models.CASCADE,default="anonymous")
    category = models.CharField(max_length=30,default="General")
    desc=models.TextField()
    date_time = models.DateTimeField(default=datetime.now())
    






