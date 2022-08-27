from django.contrib import admin
from .views import price_api
from .models import Price
# Register your models here.

class PriceAdmin(admin.ModelAdmin):
    list_display = ("DBP", "TBP")


# admin.site.register(Price, PriceAdmin)
admin.site.register(Price)
