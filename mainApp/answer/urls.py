from rest_framework import routers
from .views import AnswerViewSet

router = routers.SimpleRouter()
router.register('answer', AnswerViewSet)
urlpatterns = router.urls
