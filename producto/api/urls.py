from rest_framework.routers import DefaultRouter
from producto.api.views import productoviewset

router=DefaultRouter()
router.register('producto',productoviewset,basename='producto')
urlpatterns = router.urls

