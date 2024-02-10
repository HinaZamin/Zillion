from django.contrib import admin
from.models import Category,Customer,Product,Order
from .models import Contact
from .forms import ContactAdminForm

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)

admin.site.register(Order)


#contactform
class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm

admin.site.register(Contact)