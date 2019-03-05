from django.contrib import admin
from .models import Posts
# Register your models here.

class RegisterPostsToAdmin(admin.ModelAdmin):
    class Meta:
        model = Posts

admin.site.register(Posts,RegisterPostsToAdmin)
