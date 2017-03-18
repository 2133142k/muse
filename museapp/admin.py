from django.contrib import admin
from museapp.models import UserProfile, Comment, MusicProject
# Register your models here.
admin.site.register(Comment)
admin.site.register(MusicProject)
