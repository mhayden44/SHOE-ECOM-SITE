from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Gender)
admin.site.register(Shoe)
admin.site.register(Cart)
admin.site.register(CartItems)