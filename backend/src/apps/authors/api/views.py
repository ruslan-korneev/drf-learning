from rest_framework.viewsets import ModelViewSet

from apps.authors.models import Author, Biography, Book
from apps.authors.api.serializers import AuthorSerializer, BiographySerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
