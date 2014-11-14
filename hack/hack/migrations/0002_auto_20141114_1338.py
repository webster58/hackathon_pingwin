# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='password',
            field=models.CharField(max_length=127, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='shhkey',
            field=models.CharField(max_length=127, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='ssh_key_auth',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='user',
            field=models.CharField(max_length=127, null=True, blank=True),
            preserve_default=True,
        ),
    ]
