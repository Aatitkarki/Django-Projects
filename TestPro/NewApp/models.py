from django.db import models
from django.utils import timezone
# Create your models here.
class News(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)
    description = models.TextField()
    pub_date = models.DateField(default = timezone.now())

    def __str__(self):
        return self.author

class SportNews(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)
    description = models.TextField()

    def __str__(self):
        return self.author

class RegistrationData(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)
    phone = models.CharField(max_length = 30)

    def __str__(self):
        return self.username

