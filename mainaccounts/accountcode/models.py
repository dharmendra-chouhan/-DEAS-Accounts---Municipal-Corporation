from django.db import models

from lookup.models import Lookup,Lookupdet

class LookupManager(models.Manager):
    def get_queryset(self):
        lookup = Lookup.objects.filter(lookupcode = 'FUT').values('id')
        return super(LookupManager,self).get_queryset().filter(lookup_id=lookupid[0]['id'])


# Create your models here.
class Function_master(models.Model):
    lookup = models.ForeignKey(Lookupdet, on_delete=models.CASCADE ,related_name='Function_master')
    function_code=models.CharField(max_length=5)
    function_desc=models.CharField(max_length=200)
    function_parent_id=models.ForeignKey('self', on_delete=models.CASCADE,blank = True,null=True)
    function_compcode=models.CharField(max_length=20)
    objects = models.Manager()
    lookupmanager = LookupManager()

    class Meta:  
        db_table = "function_master"  

    def __str__(self):
        return "{}-{}".format(self.function_compcode, self.function_desc)


class Object_master(models.Model):
    lookup = models.ForeignKey(Lookupdet, on_delete=models.CASCADE,related_name='Object_master')
    object_code = models.CharField(max_length=5)
    object_desc = models.CharField(max_length=200)
    object_parent_id = models.ForeignKey('self', on_delete=models.CASCADE,blank = True,null=True)
    object_compcode = models.CharField(max_length=20)
    objects = models.Manager()
    
    class Meta:  
        db_table = "object_master"  

    def __str__(self):
        return "{}-{}".format(self.object_compcode, self.object_desc)