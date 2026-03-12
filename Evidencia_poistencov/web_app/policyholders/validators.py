from django.core.validators import RegexValidator

"""Validácia meno/priezviskom, môže obsahovať len písmena"""
letters_validator = RegexValidator(
    regex=r'^[A-Za-zÁ-Žá-ž]+$',
    message="Pole môže obsahovať len písmena"
)
"""Validácia telefonného čísla"""
phone_validator = RegexValidator(
    regex=r'^(\+421|0)[0-9]{9}$',
    message="Zadajte platné telefónne číslo (napr. 09xxxxxxx alebo +4219xxxxxxxx)."
)
"""Validácia PSČ"""
postal_code_validator = RegexValidator(
    regex=r'^\d{2}\s?\d{3}$',
    message="PSČ musí obsahovať presne 5 číslic."
)
