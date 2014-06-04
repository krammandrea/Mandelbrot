from django.db import models

# Create your models here.


# Use python manage.py migrate to create tables in connected db

# class Reporter(models.Model):
#     full_name = models.CharField(max_length=70)

#     def __str__(self): # __unicode__ on Python 2
#         return self.full_name

# class Article(models.Model):
#     pub_date = models.DateField()
#     headline = models.CharField(max_length=200) content = models.TextField()
#     reporter = models.ForeignKey(Reporter)

#     def __str__(self): # __unicode__ on Python 2 
#         return self.headline

