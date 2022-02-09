from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.authors.api.views import AuthorViewSet, BiographyViewSet, BookViewSet


router = SimpleRouter()
router.register('authors', AuthorViewSet)
router.register('biographies', BiographyViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
