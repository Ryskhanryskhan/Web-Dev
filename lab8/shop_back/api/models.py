from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 200)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.FloatField(default = 0)
    description = models.TextField(default = '')
    count = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='products', null = True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active,
        }