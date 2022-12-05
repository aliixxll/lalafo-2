from django.contrib import admin
from apps.products.models import Product,ProductImage,ProductLike,Currency
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductLike)
admin.site.register(Currency)