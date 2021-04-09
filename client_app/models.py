from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

import uuid


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    city = models.CharField(max_length=50, default=None)
    area = models.CharField(max_length=50, default=None)
    road = models.CharField(max_length=50, default=None)
    contact = models.CharField(max_length=50, default=None)
    location_coords = models.CharField(max_length=50, default=None)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.first_name


# Transactions depends on User
class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_type = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    waste_type = models.CharField(max_length=50, null=True)
    amount = models.DecimalField(max_digits=4, decimal_places=0)
    transacted_at = models.DateTimeField(default=datetime.now, blank=True)
    stars = models.IntegerField(default=0,)
    transaction_state = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.transaction_type

    class Meta:
        verbose_name_plural = "Transactions"

