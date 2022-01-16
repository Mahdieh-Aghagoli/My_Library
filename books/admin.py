from django.contrib import admin

from books.models.author import AuthorModel
from books.models.book import BookModel
from books.models.category import CategoryModel
from books.models.publication import PublicationModel


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_title', ]
    # list_display_links = ['book_title', 'isbn', ]


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_name', ]


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_title', ]


@admin.register(PublicationModel)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['pub_name', ]
