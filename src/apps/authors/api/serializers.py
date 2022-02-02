from rest_framework.serializers import ModelSerializer

from apps.authors.models import Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
