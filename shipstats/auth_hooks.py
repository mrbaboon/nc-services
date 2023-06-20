"""Define hooks for Alliance Auth like the sidebar menu entry."""

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

from . import urls


class ShipStatsMenuItem(MenuItemHook):
    """This class ensures only authorized users will see the menu entry"""

    def __init__(self):
        super().__init__(
            "shipstats",
            "fa fa-space-shuttle fa-fw",
            "shipstats:index",
            navactive=["shipstats:"],
        )

    def render(self, request):
        if request.user.has_perm("shipstats.basic_access") or True:
            return MenuItemHook.render(self, request)
        return ""


@hooks.register("menu_item_hook")
def register_menu():
    return ShipStatsMenuItem()


@hooks.register("url_hook")
def register_urls():
    return UrlHook(urls, "shipstats", "shipstats/")
