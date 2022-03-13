from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField(max_length=1000, blank=True)
    is_active = models.BooleanField(default=False)
    price = models.IntegerField()
    category = models.ForeignKey(
        "AdvertisementCategory",
        on_delete=models.SET_NULL(),
        related_name="advertisements' category",
    )
    account = models.ForeignKey(
        "Account",
        on_delete=models.SET_NULL(),
        related_name="advertisements' owner",
    )


class AdvertisementCategory(models.Model):
    title = models.CharField(max_length=120)


class AdvertisementSubCategory(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(
        "AdvertisementCategory",
        on_delete=models.CASCADE,
        related_name="subcategories",
    )


class Account(models.Model):
    firs_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=1024, blank=True)
