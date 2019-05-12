from django.db import models
from django.urls import reverse

from datetime import datetime, timedelta

from lookup.models import Lookup,Lookupdet
from subledger.models import Subledger_master
# from taggit.managers import TaggableManager

# Create your models here.
class Bankmaster(models.Model):
    bankcode = models.CharField(max_length=20)
    bankname = models.CharField(max_length=100)
    branch  = models.TextField(max_length=200)
    bankaddress = models.CharField(max_length=500)
    objects = models.Manager()
    # tags = TaggableManager()

    def __str__(self):
        return self.bankcode

    def get_absolute_url(self):
        return reverse('Bankmaster_edit', kwargs={'pk': self.pk})

class Bankmasterdet(models.Model):
        STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
        bankaccountno = models.CharField(max_length=25)
        nameofaccount = models.CharField(max_length=200)
        narration     = models.CharField(max_length=200)
        accountopeningdate =models.DateField(default=datetime.today)
        bankaccounttype =models.ForeignKey(Lookupdet, on_delete=models.CASCADE ,related_name='BANKTYPE')
        statusofaccount=models.CharField(max_length=1,choices=STATUS_CHOICES,default='Y')
        subledgeraccountcode = models.ForeignKey(Subledger_master, on_delete=models.CASCADE ,related_name='SUBLEDGER')

        def __str__(self):
           return self.bankaccountno


