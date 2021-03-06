"""Users model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from utils.models import BasicModel

class User(BasicModel, AbstractUser):
    """User model.
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_message={
            'unique':'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        massage='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.'
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blanck=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['username', 'first_name', 'last_name']

    country = models.CharField(max_length=100, blanck=False)
    city = models.CharField(max_length=100, blanck=False)

    address = models.CharField(max_length=100, blanck=False)
    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
                'Help easily distinguish users and perform queries. '
                'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address'
    )



    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username
