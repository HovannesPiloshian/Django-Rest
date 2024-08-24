from django.db import models

# Create your models here.

class House(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    number_of_rooms = models.IntegerField()
    size_in_sq_ft = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='house_images/', blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}"

    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"