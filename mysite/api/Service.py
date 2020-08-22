
from rest_framework import viewsets
from rest_framework.response import Response
from mysite.models.Author import Author
from mysite.models.Book import Book
from mysite.api.serializers import AuthorSerializer, BookSerializer

class AuthorService(viewsets.ModelViewSet):
    # 2. Specify the queryset as "all authors"
    queryset = Author.objects.all()
    # 3. Assign the serializer class
    serializer_class = AuthorSerializer


class BookService(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer