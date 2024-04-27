from django.contrib import admin
from .models import Account, Withdraw, Deposit

admin.site.register(Account)
admin.site.register(Withdraw)
admin.site.register(Deposit)

