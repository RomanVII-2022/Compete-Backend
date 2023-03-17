from django.contrib import admin
from myapp.models import Category, Blog

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog)