# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import uuid 

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for user')
    user_login=models.CharField('User',max_length=20)
    password=models.CharField('Password', max_length=30)
    email=models.EmailField('Email')
    salary = models.decimal('Salary')
    
    def __str__(self):
        return '{self.user_login}, {self.password}, {self.email}, {self.salary}'

class Category(models.Model):
    user_id=models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    description=models.CharField('Description',max_length=100)
    limit=models.decimal('Limit')
    payment = models.ManyToManyField(Payment)
    
    def __str__(self):
        return f'{self.user_id}, {self.description}, {self.limit}, {self.limit}'
    
class Payment(models.Model):
    date = models.DateField()
    price = models.decimal('Price')
    title = models.CharField('Title')
    
    def __str__(self):
        return f'{self.date}, {self.price}, {self.title}'
    