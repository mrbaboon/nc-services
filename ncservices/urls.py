from django.conf.urls import include
from allianceauth import urls
from django.urls import re_path, path

urlpatterns = [
    re_path(r"", include(urls)),
    path("__debug__/", include("debug_toolbar.urls")),
]

handler500 = "allianceauth.views.Generic500Redirect"
handler404 = "allianceauth.views.Generic404Redirect"
handler403 = "allianceauth.views.Generic403Redirect"
handler400 = "allianceauth.views.Generic400Redirect"
