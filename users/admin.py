from django.contrib import admin

from users.models import User, Order

admin.site.register(User)
admin.site.register(Order)

