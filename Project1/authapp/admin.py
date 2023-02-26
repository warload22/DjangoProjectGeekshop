from django.contrib import admin

from authapp.models import User
from basket.admin import BasketAdmin
from basket.models import Basket

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = Basket
    inlines = (BasketAdmin,)