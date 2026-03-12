from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from .validators import letters_validator,phone_validator, postal_code_validator
from django.utils import timezone

# Create your models here.
class Policyholder(models.Model):
    """Model poistenca"""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='policyholder',
    )

    first_name = models.CharField(max_length=50, validators=[letters_validator] ,verbose_name='Meno')
    last_name = models.CharField(max_length=50, validators=[letters_validator], verbose_name='Priezvisko')
    age = models.PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(120)], verbose_name='Vek')
    phone_number = models.CharField(max_length=13, validators = [phone_validator], verbose_name='Telefonné číslo')
    email = models.EmailField(max_length=100, blank=True, verbose_name='E-mail')
    street = models.CharField(max_length=100, verbose_name='Ulica')
    city = models.CharField(max_length=50, verbose_name='Mesto')
    postal_code = models.CharField(max_length=5, validators = [postal_code_validator], verbose_name='PSČ')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Policyholder"
        verbose_name_plural = "Policyholders"


class Insurance(models.Model):
    """Model poistenia"""

    policyholder = models.ForeignKey(
        Policyholder,
        on_delete=models.CASCADE,
        related_name="insurances"
    )

    """Možné typy poistenia"""
    INSURANCE_TYPES = [
        ("","Zvoľte typ poistenia"),
        ("PZP","Povinné zmluvné poistenie"),
        ("havarijne","Havarijné poistenie"),
        ("nehnutelnost","Poistenie nehnuteľnosti"),
        ("zivotne","Životné poistenie"),
        ("cestovne","Cestovné poistenie"),
    ]

    insurance_type = models.CharField(max_length=100, choices=INSURANCE_TYPES, verbose_name='Druh poistenia')
    insured_object = models.CharField(max_length=50, verbose_name='Predmet poistenia')
    description = models.TextField(blank=True, verbose_name='Popis')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Suma')
    valid_from = models.DateField(verbose_name='Začiatok platnosti')
    valid_to = models.DateField(verbose_name="Koniec platnosti")

    def __str__(self):
        return f"{self.insurance_type} ({self.policyholder})"

    class Meta:
        verbose_name = "Insurance"
        verbose_name_plural = "Insurances"
        ordering = ["-id"]

    def clean(self):
        super().clean()
        if self.valid_to and self.valid_from:
            if self.valid_to < self.valid_from:
                raise ValidationError(
                    "Dátum platnosti 'do' nemôže byť skôr ako dátum 'od'."
                )

    def save(self, *args, **kwargs):
        """Pred uložením modelu spustí všetký validácie"""
        self.full_clean()
        super().save(*args, **kwargs)

