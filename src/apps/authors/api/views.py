from rest_framework.viewsets import ModelViewSet

from apps.authors.models import Author
from apps.authors.api.serializers import AuthorSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
