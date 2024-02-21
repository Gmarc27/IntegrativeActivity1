from django.contrib import admin
from .models import Customer
from .models import Car
from .models import CarDealer
from .models import Rental

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("Customer_FirstName", "Customer_LastName", "Customer_Address")
    

class CarAdmin(admin.ModelAdmin):
    list_display = ("Car_model", "Platenumber", "Rentprice")
    

class CarDealerAdmin(admin.ModelAdmin):
    list_display = ("CarDealer_FirstName", "CarDealer_LastName")
    

class RentalAdmin(admin.ModelAdmin):
    list_display = ("Rental_Number", "Rental_Address", "Date_rent")
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Car, CarAdmin)  
admin.site.register(CarDealer, CarDealerAdmin)  
admin.site.register(Rental, RentalAdmin)