# from django import forms
# #\from .models import Student

# class StdForm(forms.Form):
#     studentID = forms.IntegerField()
#     name = forms.CharField(max_length=30)
#     major = forms.CharField(max_length=100)

from django.db import models

class StdForm(models.Model):
    studentID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    major = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'stdform'