from rest_framework import routers
from .views import SetViewSet

router = routers.DefaultRouter()
router.register('api/Set', SetViewSet, 'Surname' )

urlpatterns = router.urls



