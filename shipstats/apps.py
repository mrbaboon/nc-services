"""Django app definition."""

from django.apps import AppConfig

from . import __version__


class ShipStatsConfig(AppConfig):
    name = "shipstats"
    label = "shipstats"
    verbose_name = f"Ship Stats v{__version__}"

    def ready(self) -> None:
        from . import checks  # noqa: F401 pylint: disable=unused-import
        from . import signals  # noqa: F401 pylint: disable=unused-import
