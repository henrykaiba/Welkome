from django.db import models
from django.urls import reverse


class Post(models.Model):

    search_s = models.CharField(max_length=200, verbose_name="검색어")
    search_count = models.IntegerField(default=1, verbose_name="검색수")
    create_date = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class FAQ(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('posts:detail_faq', args=[self.pk])


class Useful(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    def get_useful_url(self):
        return reverse('posts:detail_useful', args=[self.pk])


class Contact(models.Model):

    company = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)