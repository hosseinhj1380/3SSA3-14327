from django.core.exceptions import ValidationError

def check_phone(value):
    if not (value.isnumeric() and len(value) == 11 and value.startswith("09")):
        raise ValidationError('Phone_Wrong')
