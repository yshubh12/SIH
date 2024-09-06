from django.contrib import admin
from .models import Product, FeaturedProduct, Variation
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Define resources for Product and FeaturedProduct
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        exclude = ('created_date', 'modified_date')  # Exclude auto-handled fields
        fields = ('id', 'product_name', 'slug', 'description', 'price', 'images', 'stock', 'is_available', 'category')

class FeaturedProductResource(resources.ModelResource):
    class Meta:
        model = FeaturedProduct
        exclude = ('created_date', 'modified_date')  # Exclude auto-handled fields
        fields = ('id', 'product_name', 'slug', 'description', 'price', 'images', 'stock', 'is_available', 'category')

# Extend the admin classes to include import-export functionality
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    resource_class = ProductResource  # Attach the resource to the admin

class FeaturedProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}
    resource_class = FeaturedProductResource  # Attach the resource to the admin

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

# Register the models with their respective admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(FeaturedProduct, FeaturedProductAdmin)
admin.site.register(Variation, VariationAdmin)
