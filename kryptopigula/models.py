from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField  # Import from ckeditor
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(null=True)  # Use RichTextField from ckeditor
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Editorial(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)
    content = RichTextField(null=True)  # Use RichTextField from ckeditor

    def save(self, *args, **kwargs):
        if not self.slug:
            potential_slug = slugify(self.title)
            if Editorial.objects.filter(slug=potential_slug).exists():
                i = 1
                while Editorial.objects.filter(slug=potential_slug + '-' + str(i)).exists():
                    i += 1
                self.slug = potential_slug + '-' + str(i)
            else:
                self.slug = potential_slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('editorial', args=[str(self.slug)])


    def __str__(self):
        return self.title


class CryptoAnalysis(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

# models.py
class PressRelease(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)
    content = RichTextField(null=True)  # Use RichTextField from ckeditor

    def save(self, *args, **kwargs):
        if not self.slug:
            potential_slug = slugify(self.title)
            if PressRelease.objects.filter(slug=potential_slug).exists():
                i = 1
                while PressRelease.objects.filter(slug=potential_slug + '-' + str(i)).exists():
                    i += 1
                self.slug = potential_slug + '-' + str(i)
            else:
                self.slug = potential_slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('press-release', args=[str(self.slug)])

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)
    content = RichTextField(null=True)
    views = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)


    def save(self, *args, **kwargs):
        if not self.slug:
            potential_slug = slugify(self.title)
            if News.objects.filter(slug=potential_slug).exists():
                i = 1
                while News.objects.filter(slug=potential_slug + '-' + str(i)).exists():
                    i += 1
                self.slug = potential_slug + '-' + str(i)
            else:
                self.slug = potential_slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news', args=[str(self.slug)])


    def __str__(self):
        return self.title

    
class ProcessedLink(models.Model):
    link = models.URLField(unique=True)
