from rest_framework import serializers
from mysite.models.Author import Author
from mysite.models.Book import Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    class Meta:
        model = Book
        fields = '__all__'