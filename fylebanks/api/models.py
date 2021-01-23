from django.db import models

# Create your models here.

class Bank(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=49)

    class Meta:
        db_table = "banks"

    def __str__(self):
        return f"{self.id}"


class Branch(models.Model):
    
    ifsc = models.CharField(unique=True, max_length=11)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    class Meta:
        db_table = "branches"

    def __str__(self):
        return f"{self.ifsc}"