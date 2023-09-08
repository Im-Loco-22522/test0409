from rest_framework import routers
from .views import TestResultViewSet

router = routers.SimpleRouter()
router.register('testresult', TestResultViewSet)
urlpatterns = router.urls
