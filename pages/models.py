from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200)
    tags = models.CharField(max_length=100)
    article_url = models.URLField(max_length=1024, null=True, blank=True)
