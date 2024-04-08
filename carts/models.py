from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    CHOICES = (
        ('active', 'Active'),
        ('paid', 'Paid'),
    )

    qty = models.IntegerField(_('qty'))
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='%(class)s', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='%(class)s', on_delete=models.CASCADE)
    status = models.CharField(_('status'), max_length=255, choices=CHOICES, default='Active')
    created_time = models.DateTimeField(_('created_time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time'), auto_now=True)

    class Meta:
        db_table = 'carts'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
