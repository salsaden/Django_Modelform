from __future__ import unicode_literals
from django.db import models


class StudenteMobilis(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(max_length=4)
    DoB = models.DateTimeField()
    class Meta:
        db_table="student"

