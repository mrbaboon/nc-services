from app_utils.app_settings import clean_setting

from shipstats.utils import get_unidecoded_slug

from django.utils.translation import gettext_lazy as _

SHIPSTATS_APP_NAME = clean_setting(
    "SHIPSTATS_APP_NAME", _("Ship Stats"), required_type=str
)
"""Name of this app as shown in the Auth sidebar and page titles."""

SHIPSTATS_BASE_URL = get_unidecoded_slug(SHIPSTATS_APP_NAME)
