from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet,
    LocationViewSet,
    EmployeeViewSet,
    DeviceViewSet,
)

router = DefaultRouter()
router.register("departments", DepartmentViewSet)
router.register("locations", LocationViewSet)
router.register("employees", EmployeeViewSet)
router.register("devices", DeviceViewSet)

urlpatterns = router.urls
