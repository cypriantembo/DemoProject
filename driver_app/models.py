from django.db import models
from django.contrib.auth.models import User


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    company = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)
    area = models.CharField(max_length=50, default=None)
    road = models.CharField(max_length=50, default=None)
    contact = models.CharField(max_length=50, default=None)
    location_coords = models.CharField(max_length=50, default=None)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.company




