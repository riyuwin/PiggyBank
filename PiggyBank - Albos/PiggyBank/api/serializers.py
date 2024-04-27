from rest_framework import serializers
from .models import Account, Withdraw, Deposit

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__')

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('__all__')

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('__all__')