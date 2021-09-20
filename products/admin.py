from django.contrib import admin
from .models import Product, Offer
# Register your models here.
#displaying all the details of the products by listdisplay
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

#displaying all the details of the offer by listdisplay
class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

#registering every model in admin
admin.site.register(Product, ProductAdmin)

admin.site.register(Offer, OfferAdmin)
