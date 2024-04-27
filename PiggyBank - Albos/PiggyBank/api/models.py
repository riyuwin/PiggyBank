from django.db import models

# Account model to represent user accounts
class Account(models.Model):
    accountName = models.CharField(max_length=100, unique=True)  # Field to store the account name

    def __str__(self):
        return self.accountName  # String representation of the account

# Withdraw model to represent withdrawal transactions
class Withdraw(models.Model):
    withdrawAmount = models.IntegerField()  # Field to store the withdrawal amount
    withdrawDate = models.DateField(auto_now_add=True)  # Field to store the withdrawal date (automatically set to current date)
    withdrawAccount = models.ForeignKey(Account, on_delete=models.CASCADE)  # Foreign key to relate the withdrawal to an account

    def __str__(self):
        return f"Withdraw of {self.withdrawAmount} from {self.withdrawAccount.accountName}"  # String representation of the withdrawal

# Deposit model to represent deposit transactions
class Deposit(models.Model):
    depositAmount = models.IntegerField()  # Field to store the deposit amount
    depositDate = models.DateField(auto_now_add=True)  # Field to store the deposit date (automatically set to current date)
    depositAccount = models.ForeignKey(Account, on_delete=models.CASCADE)  # Foreign key to relate the deposit to an account

    def __str__(self):
        return f"Deposit of {self.depositAmount} to {self.depositAccount.accountName}"  # String representation of the deposit
