from django.db import models



class RedditAPI(models.Model):
    title = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    author_fullname = models.CharField(max_length=255, null=True, blank=True)
    domain = models.CharField(max_length=255, null=True, blank=True) 