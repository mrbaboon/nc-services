import unidecode
from django.utils.text import slugify


def get_unidecoded_slug(app_name: str = "Ship Stats") -> str:
    """Get an unidecoded slug from a string

    :param app_name:
    :type app_name:
    :return:
    :rtype:
    """
    return slugify(unidecode.unidecode(app_name), allow_unicode=True)
