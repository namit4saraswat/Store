from email.policy import default
from tabnanny import verbose
from datetime import datetime
from django.db import models

# Create your models here.
class state(models.Model):
    state_Name = models.CharField(max_length=200 ,blank=True, verbose_name="State Name")
    city_Name = models.CharField(max_length=200, blank=True, verbose_name="City Name")
    tenderOrder = models.CharField(max_length=200, blank=True, verbose_name= "Tender Order ID")
    # status = models.BooleanField(default=1, editable=False, blank=True)
    # created_on = models.DateTimeField(default=datetime.now, editable=False, blank=True)

    def __str__(self):
        return self.state_Name + "-" +  self.city_Name

class tender(models.Model):
    tenderID = models.ForeignKey(state, on_delete=models.CASCADE, blank=True, verbose_name="Tender ID")
    # tenderExpiry = models.DateTimeField('tenderExpiry' , default=DateTime.now)
    tenderName = models.CharField(max_length=200, blank=True, verbose_name= "Tender Name")

    def __str__(self):
        return self.tenderID

class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name= "Tender Name")
    email = models.CharField(max_length=200, blank=True, verbose_name= "Email")
    query = models.CharField(max_length=200, blank=True, verbose_name= "Query Description")
    phone = models.CharField(max_length=200, blank=True, verbose_name= "Phone")
    
    def __str__(self):
        return self.name