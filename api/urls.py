from rest_framework import routers
from .views import SalaryViewSet


router = routers.DefaultRouter()
router.register(r'salary', SalaryViewSet)
