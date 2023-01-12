from rest_framework import viewsets
from django.db.models import Q

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Order.objects.filter(Q(customer__isnull=True) | Q(customer=self.request.user))
        return Order.objects.filter(customer__isnull=True)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(customer=self.request.user)
            return
        serializer.save()
