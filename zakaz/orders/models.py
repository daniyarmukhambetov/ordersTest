from django.db import models

from users.models import User


# Create your models here.

# OrderStatus = [
#     (SENT, "SENT"),
#     (REJECTED, "REJECTED"),
#     (CONTACT, "CONTACT_SOON"),
#     (ACCEPTED, "ACCEPTED")
# ]

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.IntegerField()


class OrderStatus(models.TextChoices):
    SENT = "SENT"
    REJECTED = "REJECTED"
    CONTACT = "CONTACT_SOON"
    ACCEPTED = "ACCEPTED"


class Order(models.Model):
    customer_email = models.EmailField()
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    status = models.CharField(max_length=16, choices=OrderStatus.choices, default="CONTACT_SOON")
    telephone_number = models.CharField(max_length=256)
    products = models.ManyToManyField(Product, related_name="product_orders")
