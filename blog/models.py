from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

class Shop(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = PhoneNumberField()
    address = models.TextField()
    content = models.TextField()
    photo1 = models.ImageField()
    photo2 = models.ImageField(blank=True)
    photo3 = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    shop = models.ForeignKey(Shop)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    photoshot = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)