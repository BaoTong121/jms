from django.db import models
from assets.models import Assets
from django.conf import settings


class Perms(models.Model):
    name = models.CharField(max_length=60)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    asset = models.ManyToManyField(Assets)
    comment = models.CharField(max_length=128, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

# Create your models here.
