from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as FuniRaccoon_options  

class FuniRaccoonWorld(World):
    """
    Funi Raccoon Game is a game about a Funi Raccoon who steals things.
    """
    
    game = "Funi Raccoon Game"
    web = web_world.FuniRaccoonWebWorld()

    options_dataclass = FuniRaccoon_options.FuniRaccoonOptions
    options: FuniRaccoon_options.FuniRaccoonOptions 

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Overworld"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.FuniRaccoonItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "eurosanity": self.options.eurosanity.value,
            "gemsanity":  self.options.gemsanity.value,
            "catsanity":  self.options.catsanity.value,
            "hatsanity":  self.options.hatsanity.value,
        }

    def interpret_slot_data(self, slot_data: dict) -> dict:
        for option_name in ("eurosanity", "gemsanity", "catsanity", "hatsanity"):
            if option_name in slot_data:
                getattr(self.options, option_name).value = slot_data[option_name]
        return slot_data
