from django.db import models

from assets.models import Assets
from django.conf import settings


class Perm(models.Model):
    name = models.CharField(max_length=64, verbose_name="名称")
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='用户')
    asset = models.ManyToMannuyField(Assets, verbose_name='资产')
    comment = models.CharField(max_length=128, blank=True, null=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


# Create your models here.
