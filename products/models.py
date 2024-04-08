from django.db import models
from django.utils.translation import gettext_lazy as _
from categories.models import Category

class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=_('category'), related_name='%(class)s', on_delete=models.CASCADE)
    name = models.CharField(_('name'), max_length=50)
    price = models.DecimalField(_('price'), max_digits=6, decimal_places=2)
    image = models.ImageField(_('image'), blank=True, upload_to='products/images')
    qty = models.IntegerField(_('qty'))
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name
