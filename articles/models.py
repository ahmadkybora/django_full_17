from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'))
    image = models.ImageField(_('image'), blank=True, upload_to='articles/images')

    class Meta:
        db_table = 'articles'
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.title
