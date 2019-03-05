from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    author = models.CharField(max_length = 50)


    def __str__(self):
        return self.title