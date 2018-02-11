# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from apps.location.models import City
from core.models.helpers import image_path


class UserProfile(models.Model):
    SEX_CHOICES = (
        ('Жіноча', 'female'),
        ('Чоловіча', 'male')
    )

    '''avatar = models.ImageField(
        upload_to=image_path,
        blank=True
    )
    address = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Адреса'
    )'''

    user = models.OneToOneField(
        to=User,
        related_name='profile'
    )
    sex = models.CharField(
        max_length=10,
        choices=SEX_CHOICES,
        blank=False,
        verbose_name='Стать'
    )
    phone = models.CharField(
        max_length=12,
        blank=True,
        unique=True,
        verbose_name='Номер телефону'
    )

    city = models.ForeignKey(
        to=City,
        default=1
    )

    street = models.CharField(
        verbose_name='Вулиця',
        max_length=100,
        default='',
    )

    house = models.PositiveIntegerField(
        verbose_name='Будинок',
        default=0,
    )

    house_symbol = models.CharField(
        verbose_name='Символ будинку',
        max_length=2,
        blank=True,
    )

    flat = models.PositiveIntegerField(
        verbose_name='Номер квартири',
        default=0,
    )


    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Профіль користувача'
        verbose_name_plural = 'Профілі користувачів'


class Child(models.Model):
    SEX_CHOICES = (
        ('F', 'female'),
        ('M', 'male')
    )

    first_name = models.CharField(
        max_length=20,
        blank=False,
        verbose_name="Введіть ім'я",
    )
    last_name = models.CharField(
        max_length=40,
        blank=False,
        verbose_name="Введіть прізвище",
    )
    sure_name = models.CharField(
        max_length=20,
        blank=False,
        verbose_name="Введіть по-батькові",
    )
    dob = models.DateField(
        max_length=4,
        blank =False,
        verbose_name= "вік дитини",
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        blank=False,
        verbose_name='Стать'
    )
    parents = models.ForeignKey(
        to=User,
        related_name='children',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Профіль користувача'
        verbose_name_plural = 'Профілі користувачів'
