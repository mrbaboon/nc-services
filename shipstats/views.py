import logging

from allianceauth.eveonline.models import EveCharacter
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from eveuniverse.models import EveRegion
from memberaudit.models import EveShipType, CharacterAsset, Character

logger = logging.getLogger(__name__)


def index(request):

    return render(request, "shipstats/index.html")


def ship_stats_report_data(request):
    eve_ships = EveShipType.objects.all()
    ship_assets = CharacterAsset.objects.filter(eve_type__in=eve_ships).select_related(
        "location",
        "location__eve_solar_system",
        "location__eve_solar_system__eve_constellation",
        "location__eve_solar_system__eve_constellation__eve_region",
        "character__eve_character",
        "eve_type",
        "eve_type__eve_group",
    )

    data = []
    for asset in ship_assets:

        if (
            asset.location
            and asset.location.eve_solar_system
            and asset.location.eve_solar_system.eve_constellation
        ):
            region_name = (
                asset.location.eve_solar_system.eve_constellation.eve_region.name
            )
        else:
            region_name = ""

        asset_data = {
            "type": {
                "display": asset.eve_type.name,
                "sort": asset.eve_type.name,
            },
            "group": asset.eve_type.eve_group.name,
            "location": asset.location.name if asset.location else "",
            "region": region_name,
            "corporation_name": asset.character.eve_character.corporation_name,
            "character": asset.character.eve_character.character_name,
            "main": "foo",
        }
        data.append(asset_data)

    return JsonResponse({"data": data})


def ship_stats_filters(request):

    logger.info("Received request for ship stats filters: %s", request.GET)

    region_names = list(
        EveRegion.objects.all().order_by("name").values_list("name", flat=True)
    )

    ship_types = list(
        EveShipType.objects.all().order_by("name").values_list("name", flat=True)
    )

    ship_groups = list(
        set(
            EveShipType.objects.all()
            .order_by("eve_group__name")
            .values_list("eve_group__name", flat=True)
        )
    )

    corporation_names = list(
        EveCharacter.objects.values_list("corporation_name", flat=True).distinct()
    )

    filter_data = {
        "type": ship_types,
        "region": region_names,
        "group": sorted(ship_groups),
        "corporation_name": sorted(corporation_names),
    }

    return JsonResponse(filter_data)
