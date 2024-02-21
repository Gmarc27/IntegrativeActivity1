from django.db import models

# Create your models here.

class Customer(models.Model):
    Customer_FirstName = models.CharField('FirstName', max_length=120)
    Customer_LastName = models.CharField('LastName', max_length=120)
    Customer_MiddleName = models.CharField('MiddleName', max_length=120)
    Customer_LicenseNo = models.FloatField(blank=True)
    Customer_Emailadd = models.EmailField('Email Address', max_length=255, blank=True, null=True)
    Customer_Address = models.CharField('Address', max_length=120)
    Customer_Age = models.IntegerField()
    Customer_Gender = models.CharField('Gender', max_length=32)
    
    def __str__(self):
        return f"{self.Customer_FirstName} {self.Customer_LastName} {self.Customer_Address}"

class Car(models.Model):
    Car_model = models.CharField('FirstName', max_length=120)
    Platenumber = models.FloatField(blank=True)
    Rentprice = models.IntegerField()
    Odometer = models.FloatField(blank=True)
    Year = models.IntegerField()
    Condition = models.TextField(blank=True, null = True)
    
    def __str__(self) :
        return f"{self.Car_model}"

class CarDealer(models.Model):
    CarDealer_FirstName = models.CharField('FirstName', max_length=120)
    CarDealer_LastName = models.CharField('LastName', max_length=120)
    CarDealer_MiddleName = models.CharField('MiddleName', max_length=120)
    CarDealer_Emailadd = models.EmailField('Email Address', max_length=255, blank=True, null=True)
    CarDealer_Pass = models.CharField('Password', max_length=120)
    
    def __str__(self):
        return f"{self.CarDealer_FirstName} {self.CarDealer_LastName}"
    
class Rental(models.Model):
    Rental_Number = models.FloatField(blank=True)
    Rental_Address = models.CharField('Address', max_length=120)
    Date_rent = models.DateTimeField(auto_now_add=True)
    Date_return = models.DateTimeField(auto_now=True)
    Destination = models.TextField(blank=True, null = True)
    Payment = models.IntegerField()
    
    def __str__(self):
        return f"{self.Rental_Number} {self.Rental_Address} {self.Date_rent}"
    