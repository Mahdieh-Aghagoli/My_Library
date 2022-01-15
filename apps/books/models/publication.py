from django.db import models

from django.utils.translation import gettext_lazy as _


class PublicationModel(models.Model):
    pub_name = models.CharField(_('Publication'), max_length=200, unique=True)
    pub_info = models.TextField(_('Information'), null=True, blank=True)

    # pub_logo = models.ImageField(_('Logo'), null=True, blank=True)

    class Meta:
        ordering = ['pub_name']

    def __str__(self):
        return self.pub_name
