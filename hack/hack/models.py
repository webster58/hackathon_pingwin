from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    ip = models.CharField(max_length=127, null=True, blank=True)
    country = models.CharField(max_length=127, null=True, blank=True)
    user = models.CharField(max_length=127, null=True, blank=True)
    password = models.CharField(max_length=127, null=True, blank=True)
    shhkey = models.CharField(max_length=127, null=True, blank=True)
    ssh_key_auth = models.BooleanField (default = False)


    def __unicode__(self):  # Python 3: def __str__(self):
        return u'(%d) - %s ' % (self.pk, self.name)
