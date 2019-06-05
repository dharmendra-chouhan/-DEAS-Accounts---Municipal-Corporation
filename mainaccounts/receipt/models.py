from __future__ import unicode_literals
from django.urls import reverse

from subledger.models import Subledger_master

from django.db import models
from django.utils import timezone


class Receipt(models.Model):
    receipt_no = models.CharField(max_length=20)
    receipt_date = models.DateTimeField(default=timezone.now)
    payer_name = models.CharField(max_length=200)
    narration = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('receipt-update', kwargs={'pk': self.pk})

    def __unicode__(self):
        return "%s %s" % (self.receipt_no, self.receipt_date)


class Receiptdet(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    subledger_master =models.ForeignKey(Subledger_master, on_delete=models.CASCADE,related_name='subledger')
    receipt_amt = models.DecimalField(decimal_places=2,max_digits=15)

