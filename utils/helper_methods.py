from random import choice
from string import ascii_letters, digits

from django.conf import settings

AVAILABLE_CHARS = ascii_letters + digits

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 10)


def create_random_code(characters=AVAILABLE_CHARS):
    code = "".join([choice(characters) for _ in range(SIZE)])
    return code


def create_shorted_url(model_instance):
    random_code = create_random_code()
    model_class = model_instance.__class__
    if model_class.objects.filter(short_url=random_code).exists():
        return create_shorted_url(model_instance)
    return random_code
