from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify, stringformat
import markdown
import re
from bs4 import BeautifulSoup


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.TextField()
    content_html = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={
            'year': self.date.year,
            'month': stringformat(self.date.month, '02d'),
            'day': stringformat(self.date.day, '02d'),
            'slug': self.slug
        })

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Post)
def pre_save_post(**kwargs):
    content_html = markdown.markdown(kwargs['instance'].content,
                                     extensions=['codehilite'])
    soup = BeautifulSoup(content_html)
    for tag in soup.find_all(re.compile(r'h\d')):
        if tag.parent is soup:
            tag.name = 'h%d' % (int(tag.name[1]) + 1)
    kwargs['instance'].content_html = str(soup)
    kwargs['instance'].slug = slugify(kwargs['instance'].title)
