from django.urls import path

import shipstats.views

app_name = "shipstats"

urlpatterns = [
    path("", shipstats.views.index, name="index"),
    path(
        "reports/data/ship-stats/",
        shipstats.views.ship_stats_report_data,
        name="ship_stats_report_data",
    ),
    path(
        "reports/data/ship-stats/filters/",
        shipstats.views.ship_stats_filters,
        name="ship_stats_filters",
    ),
]
