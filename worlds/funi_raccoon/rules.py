from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule

from .items import ITEM_NAME_TO_ID

if TYPE_CHECKING:
    from .world import FuniRaccoonWorld

# All items with IDs in the 1-175 range are the "real" collectible items.
COLLECTIBLE_ITEMS = [name for name, item_id in ITEM_NAME_TO_ID.items() if 1 <= item_id <= 175]


def set_all_rules(world: FuniRaccoonWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: FuniRaccoonWorld) -> None:
    victory = world.get_location("Victory")
    set_rule(victory, lambda state: state.count_from_list(COLLECTIBLE_ITEMS, world.player) >= 100)


def set_completion_condition(world: FuniRaccoonWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
