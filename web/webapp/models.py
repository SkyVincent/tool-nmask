# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class dianzan_table(models.Model):
	tool_name = models.CharField(max_length=100)
	number = models.IntegerField()


class auth(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)