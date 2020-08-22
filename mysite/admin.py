from django.contrib import admin

# Register your models here.
from .models.Author import Author
from .models.Book import Book

classes = [Author, Book]

for model in classes:
    admin.site.register(model)