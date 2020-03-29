from django.db import models

class Assets(models.Model):
    OS_CHOICE = [
        ('C', 'CentOS'),
        ('U', 'Ubuntu'),
        ('D', 'Debian'),
        ('R', 'Redhat'),
        ('W', 'Windows'),
    ]
    hostname = models.CharField(verbose_name='Hostname', unique=True, max_length=128)
    ip = models.GenericIPAddressField(verbose_name='IP', unique=True)
    port = models.IntegerField(default=22, verbose_name='端口')
    username = models.CharField(max_length=20, verbose_name='管理员用户名')
    password = models.CharField(max_length=2, verbose_name='管理员密码')
    os = models.CharField(choices=OS_CHOICE, max_length=2, verbose_name='系统平台', default="C")
    is_active = models.BooleanField(default=True, verbose_name="是否激活")

    def __str__(self):
        return self.ip
# Create your models here.
