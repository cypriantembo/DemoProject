from django.contrib import admin

from .models import Client, Transactions
# Register your models here.

admin.site.register(Client)
admin.site.register(Transactions)


