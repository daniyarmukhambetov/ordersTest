from django.urls import path, include
from rest_framework import routers

from .views import OrderViewSet

router = routers.DefaultRouter()

router.register("orders", OrderViewSet, basename="orders")

urlpatterns = router.urls
