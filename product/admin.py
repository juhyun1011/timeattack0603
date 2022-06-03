from django.contrib import admin
from .models import DrinkModel, CategoryModel
# Register your models here.
admin.site.register(DrinkModel)
admin.site.register(CategoryModel)