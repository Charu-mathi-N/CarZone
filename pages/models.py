from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    designation = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    facebook = models.URLField(max_length=60)
    twitter = models.URLField(max_length=60)
    google_plus = models.URLField(max_length=60)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name