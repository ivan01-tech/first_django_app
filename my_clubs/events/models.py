from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField("Venue Name", max_length=120)
    zip_code = models.CharField("Zip Code", max_length=120)
    email_address = models.EmailField("Venue Email")
    address = models.CharField(max_length=300)
    web = models.URLField("Web site",blank=True,null=True)
    phone = models.CharField("Phone Number", max_length=50,blank=True,null=True)

    def __str__(self) -> str:
        return self.name


class MyClubsUser(models.Model):
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    email_address = models.EmailField("User Email")
    
    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"

class Event(models.Model):
    name = models.CharField("Event Name", max_length=120, blank=True, null=True)
    event_date = models.DateTimeField("Event Date")
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    manager = models.ForeignKey(User, blank=True, null=True,on_delete=models.SET_NULL)
    description = models.TextField(blank=True, null=True)
    attendees = models.ManyToManyField(MyClubsUser,blank=True)
    
    def __str__(self) -> str:
        return self.name
