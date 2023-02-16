from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxValueValidator, MinValueValidator, URLValidator)
from django.utils.translation import gettext_lazy as _


TYPE = (
    (1, 'Environment'),
    (2, 'Sports'),
    (3, 'Medical'),
    (4, 'Disaster relief'),
    (5, 'Anti-corruption'),
    (6, 'Peace'),
    (7, 'Humanitarian'),
    (8, 'Technology'),
    (9, 'Education'),
    (10, 'Regulatory'),
    (11, 'Religious'),
    (12, 'Ethics'),
    (13, 'Policy'),
    (14, 'Governance'),
    (15, 'Youth'),
    (16, 'Legal'),
    (17, 'Democracy'),
    (18, 'Other')
    )

REGION = (
    (1, 'Worldwide'),
    (2, 'Europe'),
    (3, 'North America'),
    (4, 'Central America'),
    (5, 'South America'),
    (6, 'Asia'),
    (7, 'Africa'),
    (8, 'Oceania'),
    (9, 'Middle East')
)


def validate_type(value):
    """
    Validation for primary model type field
    """
    if value < 1:
        raise ValidationError(
            _('%(value)s is less than 1'),
            params={'value': value},
        )
    elif value > TYPE.length:
        raise ValidationError(
            _(f'%(value)s is greater than {TYPE.length}'),
            params={'value': value},
        )


def validate_region(value):
    """
    Validation for primary model region field
    """
    if value < 1:
        raise ValidationError(
            _('%(value)s is less than 1'),
            params={'value': value},
        )
    elif value > REGION.length:
        raise ValidationError(
            _(f'%(value)s is greater than {REGION.length}'),
            params={'value': value},
        )


class NGO(models.Model):
    """
    Primary model for an NGO
    location field is a town, city, etc
    headquarters is a building or institution - MIT, CalTech, 55 Tufton Street
    (55 Tufton Street is full of crooks and conmen)
    """
    name = models.CharField(max_length=200)
    type = models.IntegerField(choices=TYPE, default=18, validators=[validate_type])
    founded = models.DateField(auto_now_add=False)
    founders = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    staff = models.IntegerField(validators=[MinValueValidator(1)])
    region = models.IntegerField(choices=REGION, default=1, validators=[validate_region])
    location = models.CharField(max_length=200)
    headquarters = models.CharField(max_length=200)
    website = models.URLField(validators=[URLValidator()])
    image = CloudinaryField('image', default='placeholder')
    purpose = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        """
        Meta class for Ngo model
        """
        ordering = ['-founded']
        verbose_name = "Non-governmental organisation"

    def __str__(self):
        """
        Magic string method
        """
        return f"{self.name}"
