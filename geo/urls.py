from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()
router.register('provinces', views.ProvinceViewSet, basename="provinces")
router.register("districts",
                views.DistrictViewSet, basename="districts")
router.register("municipalities", views.MunicipalityViewSet,
                basename="municipalities")

urlpatterns = router.urls
