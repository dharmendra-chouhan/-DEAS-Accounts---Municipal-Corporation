from django.db import models
from datetime import datetime, timedelta
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from lookup.models import Lookup,Lookupdet
from accountcode.models import Function_master,Object_master
from django.urls import reverse


class LookupManager(models.Manager):
    def get_queryset(self):
        lookup = Lookup.objects.filter(lookupcode = 'DRCR').values('id')
        lookupdet =Lookupdet.objects.filter(lookup_id=lookup[0]['id']).values()
        return super(LookupManager,self).get_queryset().filter(lookupdet_opening_drcr=lookupdet[0]['id'])


# Create your models here.
class Subledger_master(models.Model):
    #     STATUS_CHOICES = (
    #     ('A', 'Active'),
    #     ('I', 'Inactive'),
    # )
    #     BUDGET_CHOICES = (
    #     ('Y', 'Yes'),
    #     ('N', 'No'),  
    # )
        function_id = models.ForeignKey(Function_master, on_delete=models.CASCADE,related_name='Function')
        object_id = models.ForeignKey(Object_master, on_delete=models.CASCADE ,related_name='Object')
        lookupdet_bug= models.ForeignKey(Lookupdet, on_delete=models.CASCADE ,related_name='Budget')
        opening_bal = models.DecimalField(default=None, blank=True, null=True, decimal_places=2,max_digits=15)
        lookupdet_opening_drcr = models.ForeignKey(Lookupdet, on_delete=models.CASCADE ,related_name='Lookupdet', default=None, blank=True, null=True)
        opening_bal_date =models.DateField(default=None, blank=True, null=True)
        subledger_code=models.CharField(max_length=20)
        subledger_desc=models.CharField(max_length=200)
        status = models.ForeignKey(Lookupdet, on_delete=models.CASCADE ,related_name='Lookupdet_status')
        budget_provion_required = models.ForeignKey(Lookupdet, on_delete=models.CASCADE ,related_name='Lookupdet_budget')
        objects = models.Manager()
        lookupmanager = LookupManager()


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Save Ledger'))