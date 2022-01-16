from django.contrib import admin

from user.models import AccountModel


@admin.register(AccountModel)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username']
