from django.contrib import admin
from . models import Brand
# Register your models here.


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('BrandName',)}
    list_display = ['BrandName', 'slug']

admin.site.register(Brand, BrandAdmin)