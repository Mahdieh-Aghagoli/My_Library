from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

from apps.books.models.author import AuthorModel
from apps.books.models.category import CategoryModel
from apps.books.models.publication import PublicationModel
from common.constants import BOOK_TYPE_CHOICES, BOOK_LANGUAGE_CHOICES
from common.validators import isbn_validator


class BookModel(models.Model):
    isbn = models.CharField(_('ISBN'), isbn_validator, max_length=13, primary_key=True)
    book_title = models.CharField(_('Book Title'), max_length=300, unique=True)
    book_author = models.ManyToManyField(AuthorModel)
    book_cat = models.ManyToManyField(CategoryModel)
    bok_lang = models.CharField(_('Language'), choices=BOOK_LANGUAGE_CHOICES, max_length=2, default='EN')
    book_pub = models.ForeignKey(PublicationModel, on_delete=models.CASCADE)
    book_edition = models.CharField(_('Edition'), max_length=20)
    book_info = models.TextField(_('Information'), blank=True, null=True)
    book_awards = models.CharField(_('Awards'), max_length=500, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    book_type = models.CharField(_('Book Type'), choices=BOOK_TYPE_CHOICES, max_length=2, default='PB')
    slug = AutoSlugField(populate_from=[book_title, isbn])

    # things that can be inherited from another app
    book_comment = models.TextField(_('Comment'), blank=True, null=True)
    book_fav = models.BooleanField(_('Favorite'), default=False)

    class Meta:
        verbose_name = [_('Book')]
        verbose_name_plural = [_('Books')]
