from django.db import models

from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    cat_title = models.CharField(_('Category'), max_length=300)

    # things that can be inherited from another app
    cat_comment = models.TextField(_('Comment'), blank=True, null=True)
    cat_fav = models.BooleanField(_('Favorite'), default=False)

    class Meta:
        verbose_name = [_('Category')]
        verbose_name_plural = [_('Categories')]
