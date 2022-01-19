from django.db import models
from django.db.models.fields import BigIntegerField

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    account_no = models.CharField(max_length=122)
    amount = models.IntegerField()
    city = models.CharField(max_length=122)
    mobile_no = BigIntegerField()
    def __str__(self):
        return self.name

class transaction_details(models.Model):
    source_name = models.CharField(max_length=122)
    source_acc_no = models.CharField(max_length=122)
    Current_balance = models.IntegerField()
    money_deposit = models.IntegerField()
    destination_name = models.CharField(max_length=122)
    date = models.DateField()
