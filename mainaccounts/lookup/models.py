from django.db import models

# Create your models here.


# SELECT * FROM PUBLIC.lookup_lookupdet WHERE lookup_id= (select id from PUBLIC.lookup_lookup where lookupcode='HOT') order by id

class Lookup(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('Inactive', 'inactive'),
    )

    lookupcode = models.CharField(max_length=30)
    lookname = models.CharField(max_length=100)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='active')
    
    def __str__(self):
        return "%s %s" % (self.lookupcode, self.lookname)

class Lookupdet(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('Inactive', 'inactive'),
    )

    lookupdetdesc = models.CharField(max_length=200)
    lookupvalue = models.CharField(max_length=100)
    lookuplevel = models.PositiveSmallIntegerField(default=0)
    lookup = models.ForeignKey(Lookup, on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='active')
    objects = models.Manager()
    def __str__(self):
        return self.lookupdetdesc

    class Meta:
        ordering = ('lookupdetdesc',)


