# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreBoard',
            fields=[
                ('Username', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Prob1', models.IntegerField(default=0)),
                ('Prob2', models.IntegerField(default=0)),
                ('Prob3', models.IntegerField(default=0)),
                ('Prob4', models.IntegerField(default=0)),
                ('Prob5', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
