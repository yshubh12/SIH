from django.db import models
from category.models import Category
from django.urls import reverse
from django.utils.text import slugify

class BaseProduct(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class Product(BaseProduct):
    pass


class FeaturedProduct(BaseProduct):
    def save(self, *args, **kwargs):
        # Save the FeaturedProduct instance
        super().save(*args, **kwargs)
        
        # Ensure that the FeaturedProduct is also saved as a Product
        product, created = Product.objects.get_or_create(
            product_name=self.product_name,
            defaults={
                'slug': self.slug,
                'description': self.description,
                'price': self.price,
                'images': self.images,
                'stock': self.stock,
                'is_available': self.is_available,
                'category': self.category,
                'created_date': self.created_date,
                'modified_date': self.modified_date,
            }
        )
        if not created:
            # Update existing Product fields if the Product already exists
            product.slug = self.slug
            product.description = self.description
            product.price = self.price
            product.images = self.images
            product.stock = self.stock
            product.is_available = self.is_available
            product.category = self.category
            product.save()


class VariationManager(models.Manager):
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)

variation_category_choice = (
    ('size', 'size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value
