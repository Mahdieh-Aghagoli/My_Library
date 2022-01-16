from django.db import models

from django.utils.translation import gettext_lazy as _


class AuthorModel(models.Model):
    author_name = models.CharField(_('Author'), max_length=200, unique=True)
    author_info = models.TextField(_('Information'), null=True, blank=True)
    author_pic = models.ImageField(_('Picture'), null=True, blank=True)

    # things that can be inherited from another app
    author_comment = models.TextField(_('Comment'), blank=True, null=True)
    author_fav = models.BooleanField(_('Favorite'), default=False)

    class Meta:
        verbose_name = [_('Author')]
        verbose_name_plural = [_('Authors')]

    def __str__(self):
        return self.author_name
