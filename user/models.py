import pyotp as pyotp
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

from common.validators import username_validator, phone_validator
from user.managers import AccountManager


def my_slugify_function(content):
    return slugify(content, allow_unicode=True)


class AccountModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Username'), validators=[username_validator], max_length=25, unique=True)
    email = models.EmailField(_('Email'), unique=True)
    name = models.CharField(_('Name'), max_length=100, blank=True, null=True)
    lastname = models.CharField(_('Last Name'), max_length=100, blank=True, null=True)
    phone_number = models.CharField(_('Phone Number'), validators=[phone_validator], max_length=11, blank=True,
                                    null=True)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, null=True)
    avatar = models.ImageField(_('Avatar'), blank=True, null=True)
    date_of_birth = models.DateField(_('Date of Birth'), blank=True, null=True,
                                     help_text=_('Please use the follow format :<em>YYYY-MM-DD</em>'))
    otp = models.CharField(max_length=8, unique_for_date=True, blank=True, null=True)
    slug = AutoSlugField(populate_from=['username'], unique=True, allow_unicode=True,
                         slugify_function=my_slugify_function)
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_superuser = models.BooleanField(_('Superuser'), default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_fullname(self):
        return self.name + ' ' + self.lastname

    def otp_func(self, otp):
        t = pyotp.TOTP(self.otp, interval=120)
        return t.verify(otp)
