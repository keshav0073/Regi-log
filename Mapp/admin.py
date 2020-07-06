from django.contrib import admin
from .models import phone_info
# Register your models here.
class adminphone(admin.ModelAdmin):
    list_display = ('name','number')


admin.site.register(phone_info,adminphone)