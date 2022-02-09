from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from apps.authors.models import Author, Biography, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Biography
        fields = ('text', 'author')


class BookSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'authors')
