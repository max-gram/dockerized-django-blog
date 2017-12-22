from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from datetime import datetime

# POSTS
@python_2_unicode_compatible
class Post(models.Model):
    slug = models.SlugField('Slug', unique=True, max_length=255)
    previewText = models.CharField('Preview Txt', max_length=255)
    title = models.CharField('Title', max_length=255)
    body = models.TextField('Body', max_length=5000)
    is_published = models.BooleanField('Published', default=True)
    pub_date = models.DateTimeField('Date Published', default=datetime.now)

    class Meta:
        ordering = ['-pub_date']
        verbose_name='Blog Post'
        verbose_name_plural='All Posts'

    def __str__(self):
        return "%s" % self.title
