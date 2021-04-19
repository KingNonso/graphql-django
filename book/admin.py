from django.contrib import admin

from book.models import Category, Ingredient

admin.site.register(Category)
admin.site.register(Ingredient)