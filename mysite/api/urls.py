from rest_framework.routers import DefaultRouter

from .Service import AuthorService, BookService

router = DefaultRouter()
app_name = 'mysite-api'

router.register(r'authors', AuthorService)
router.register(r'books', BookService)
urlpatterns = router.urls