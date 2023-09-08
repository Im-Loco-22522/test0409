from rest_framework import routers
from .views import TestViewSet

router = routers.SimpleRouter()
router.register('test', TestViewSet)
urlpatterns = router.urls
