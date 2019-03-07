from django.db import models

# Create your models here.
class Posts(models.Model):
    created_at = models.DateTimeField(auto_now = True, blank= True)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    author = models.CharField(max_length = 50)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"


