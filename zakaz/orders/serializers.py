from rest_framework import serializers
from django.db.models import Sum
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from .models import Order, Product


@extend_schema_field(OpenApiTypes.STR)
class ProductRelatedField(serializers.RelatedField):
    default_error_messages = {
        "incorrect_type": "Incorrect type. Expected a string, but got {input_type}",
        "does_not_exist": "Product with name '{product_name}' does not exits"
    }

    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        if not isinstance(data, str):
            self.fail("incorrect_type", input_type=type(data).__name__)
        try:
            return Product.objects.get(name=data)
        except Product.DoesNotExist:
            return self.fail("does_not_exist", product_name=data)


class OrderSerializer(serializers.ModelSerializer):
    products = ProductRelatedField(many=True, required=True, read_only=False, queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = [
            "customer_email",
            "telephone_number",
            "status",
            "products",
        ]
        read_only_fields = [
            "status",
        ]
