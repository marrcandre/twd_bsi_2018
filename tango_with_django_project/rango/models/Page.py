from django.db import models
from .Category import Category


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='pages')
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title