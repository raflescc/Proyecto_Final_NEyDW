from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='artworks/')
    stock = models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
