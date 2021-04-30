from django.db import models


# Create your models here.
class Mobile(models.Model):
    part_number = models.CharField(max_length=120, unique=True)
    manufacturer = models.CharField(max_length=100)
    mobile_name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.FloatField(max_length=50)
    mob_image = models.ImageField(upload_to='images')
    specification = models.TextField(max_length=200)

    def __str__(self):
        return self.model_number


class Buyer(models.Model):
    STATUS = (
        ('NO', 'NewOrder'),
        ('P', 'Packing'),
        ('D', 'Dispatch'),
        ('CD', 'Complete Deleivery'),
)
    buyer_name = models.CharField(max_length=100)
    buyer_address = models.TextField(max_length=300)
    buyer_mobile = models.CharField(max_length=100)
    product = models.CharField(max_length=120, null=True)
    user = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=2, null=True,choices=STATUS)

    def __str__(self):
        return self.status
