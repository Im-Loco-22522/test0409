from rest_framework import routers
from .views import QuestionViewSet

router = routers.SimpleRouter()
router.register('question', QuestionViewSet)
urlpatterns = router.urls
