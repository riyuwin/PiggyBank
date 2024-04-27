from rest_framework import generics

from .models import Account, Withdraw, Deposit  # Importing your Django models
from .serializers import AccountSerializer, WithdrawSerializer, \
    DepositSerializer  # Importing serializers for your models


# Endpoint for listing and creating accounts
class AccountList(generics.ListCreateAPIView):
    serializer_class = AccountSerializer  # Using AccountSerializer for serialization

    # Customizing queryset based on query parameters
    def get_queryset(self):
        queryset = Account.objects.all()  # Fetching all accounts initially
        withdraw = self.request.query_params.get('withdraw')  # Getting 'withdraw' query parameter
        deposit = self.request.query_params.get('deposit')  # Getting 'deposit' query parameter

        # Filtering queryset if 'withdraw' parameter is provided
        if withdraw is not None:
            queryset = queryset.filter(withdrawAccount=withdraw)

        # Filtering queryset if 'deposit' parameter is provided
        if deposit is not None:
            queryset = queryset.filter(depositAccount=deposit)


# Endpoint for retrieving, updating, and deleting a specific account
class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer  # Using AccountSerializer for serialization
    queryset = Account.objects.all()  # Fetching all accounts initially


# Endpoint for listing and creating withdraw transactions
class WithdrawList(generics.ListCreateAPIView):
    serializer_class = WithdrawSerializer  # Using WithdrawSerializer for serialization
    queryset = Withdraw.objects.all()  # Fetching all withdraw transactions initially


# Endpoint for retrieving, updating, and deleting a specific withdraw transaction
class WithdrawDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WithdrawSerializer  # Using WithdrawSerializer for serialization
    queryset = Withdraw.objects.all()  # Fetching all withdraw transactions initially


# Endpoint for listing and creating deposit transactions
class DepositList(generics.ListCreateAPIView):
    serializer_class = DepositSerializer  # Using DepositSerializer for serialization
    queryset = Deposit.objects.all()  # Fetching all deposit transactions initially


# Endpoint for retrieving, updating, and deleting a specific deposit transaction
class DepositDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DepositSerializer  # Using DepositSerializer for serialization
    queryset = Deposit.objects.all()  # Fetching all deposit transactions initially
