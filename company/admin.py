from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(ContactList)
admin.site.register(Profile)
admin.site.register(ResetPasswordToken)
admin.site.register(Action)
