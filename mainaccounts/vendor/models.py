from django.db import models
from django.urls import reverse

# from taggit.managers import TaggableManager

# Create your models here.
class Vendor(models.Model):
    vid = models.CharField(max_length=20)
    vname = models.CharField(max_length=100)
    vaddress  = models.TextField(max_length=200)
    vemail = models.EmailField()
    vcontact = models.CharField(max_length=15)
    objects = models.Manager()
    # tags = TaggableManager()

    def __str__(self):
        return self.vid

    def get_absolute_url(self):
        return reverse('vendor_edit', kwargs={'pk': self.pk})



        

