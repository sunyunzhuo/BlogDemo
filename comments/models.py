# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    article = models.ForeignKey('article.Article')

    def __unicode__(self):
        return self.text[:20]