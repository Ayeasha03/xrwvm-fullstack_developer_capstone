from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.




# CarModelInline class
class CarModelInline(admin.TabularInline):  # or admin.StackedInline
    model = CarModel
    extra = 1

# CarModelAdmin class
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

# CarMakeAdmin class with CarModelInline

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)
