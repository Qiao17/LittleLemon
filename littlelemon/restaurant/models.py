from django.db import models

# Create your models here.
class Menu(models.Model):
    #ID = models.IntegerField()
    Title = models.CharField(max_length=500)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Inventory = models.IntegerField()
    
    def __str__(self):
        return self.Title 

class Booking(models.Model):
   # ID = models.IntegerField()
    Name = models.CharField(max_length=500)
    No_of_guest = models.IntegerField()
    BookingDate = models.DateTimeField()
    def __str__(self):
        return self.Name 