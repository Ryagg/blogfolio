from django.db import models

STATUS = (
    (0, 'Submitted'),
    (1, 'Published'),
)


class Article(models.Model):
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200)
    tags = models.CharField(max_length=100)
    article_url = models.URLField(max_length=1024, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
