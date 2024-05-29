from django.db import models
from django.apps import apps
from base.models import BaseModel


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_desription = models.TextField()

    def __str__(self) -> str:
        return self.product_name
    
    def get_review_count(self):
        Review = apps.get_model('accounts', 'Review')
        return Review.objects.filter(product=self).count()


class ProductImage(BaseModel):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
    image =  models.ImageField(upload_to="product")