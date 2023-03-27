from django.contrib import admin

# Register your models here.

from .models import Order
class OrderAdmin(admin.ModelAdmin):
  list_display = ("title", "prodCode", "custCode",)
admin.site.register(Order,OrderAdmin)
