from django.contrib import admin
from .views import price_api
from .models import Price
# Register your models here.


class PriceAdmin(admin.ModelAdmin):
    instance = Price.objects.all()
    list_display = ("DBP", "TBP","calc_price")


admin.site.register(Price,PriceAdmin)
