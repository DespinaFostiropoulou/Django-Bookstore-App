from django.conf import settings
from django.db import models
from django.utils import timezone

class Book(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titlos = models.CharField(max_length=50)
    tipos = models.ForeignKey('tipos', null=True, on_delete=models.CASCADE)
    syggrafeas = models.ForeignKey('syggrafeas', null=True, on_delete=models.CASCADE)
    ekdotikos_oikos = models.ForeignKey('ekdotikos_oikos', null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    perilipsi = models.TextField(null=True)
    image = models.ImageField(null=True)
    timi = models.TextField(null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titlos

class tipos(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class syggrafeas(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class ekdotikos_oikos(models.Model):
    Name = models.CharField(max_length=100)


    def __str__(self):
        return self.Name