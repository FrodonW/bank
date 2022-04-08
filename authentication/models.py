# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


# class Customer(models.Model):
#     STAFF = 1
#     CUSTOMER = 2
#     ROLE_CHOICES = [
#         (STAFF, _('Staff')),
#         (CUSTOMER, _('Customer'))
#     ]
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     is_customer = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, default=2)
