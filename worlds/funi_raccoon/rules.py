from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasFromList

from .items import ITEM_NAME_TO_ID
from .locations import LOCATION_NAME_TO_ID

if TYPE_CHECKING:
    from .world import FuniRaccoonWorld

# Items that have a "Store X" dumpster location. Store location IDs follow the pattern
# location_id == item_id + 1000, so this excludes Euros, strength upgrades, truck
# upgrades, and anything else that isn't deposited at the dumpster.
_STORE_LOCATION_IDS = {loc_id for loc_id in LOCATION_NAME_TO_ID.values() if 1001 <= loc_id <= 1999}
DUMPSTER_ITEMS = [
    name for name, item_id in ITEM_NAME_TO_ID.items()
    if (item_id + 1000) in _STORE_LOCATION_IDS
]

# Progressive Mystical Dumbbell requirements per store location.
# TINY (weight 1) items have no requirement and are omitted.
# SMALL=1, MEDIUM=2, HEAVY=3, CHUNKY=4.
_DUMBBELL_REQUIREMENTS: dict[str, int] = {
    # SMALL (weight 2) — requires 1 dumbbell
    "Store Funbells":                            1,
    "Store Vending Machine (accepts doubloons)": 1,
    "Store Washing Machine":                     1,
    "Store Buisness Man":                        1,
    "Store Paracetamol 650mg":                   1,
    "Store Heavy Stone Torch":                   1,
    "Store Sign":                                1,
    "Store Pirate":                              1,
    "Store Pirate 2":                            1,
    "Store Pirate 3":                            1,
    "Store Feral Dog":                           1,
    "Store Beenie, Our Savior":                  1,
    "Store Patrick O'Hara":                      1,
    "Store Crisp":                               1,
    "Store Divider":                             1,
    "Store My Favourite Chair":                  1,
    "Store Blimbo Village Sign":                 1,
    "Store Papa Tyre":                           1,
    "Store Broken Truck":                        1,
    "Store CHEESE":                              1,
    "Store Trolley":                             1,
    "Store Folding Chair":                       1,
    "Store Pickaxe":                             1,
    "Store Fone":                                1,
    "Store Coffee Cup":                          1,
    "Store Kettle":                              1,
    "Store Flower Blimbo":                       1,
    "Store Cheeky Pint":                         1,
    "Store CD Player":                           1,
    "Store Anti Sads":                           1,
    "Store Old Sign":                            1,
    "Store Warning Sign":                        1,
    "Store Ms. Heel":                            1,
    "Store Mr. Heel":                            1,
    "Store Priestess":                           1,
    "Store Beenie Saves The Orphans":            1,
    "Store Milk Klubnika":                       1,
    "Store Wriks Celler":                        1,
    "Store Door":                                1,
    "Store Goo Container":                       1,
    # MEDIUM (weight 3) — requires 2 dumbbells
    "Store Crack Head":                          2,
    "Store Microwave":                           2,
    "Store Logan Left":                          2,
    "Store Logan Right":                         2,
    "Store Crisps Undying Love":                 2,
    'Store "Cow"':                               2,
    "Store Gas Drum":                            2,
    "Store Smoker":                              2,
    "Store Radiator":                            2,
    "Store Bench":                               2,
    "Store Bin":                                 2,
    "Store Knifedog":                            2,
    "Store Suitcase":                            2,
    "Store Flowian":                             2,
    "Store Bell Boy":                            2,
    "Store Demon Core":                          2,
    "Store Gas Pumpo":                           2,
    "Store Radio Blimbo":                        2,
    "Store Manhole Cover":                       2,
    "Store Eel Can":                             2,
    "Store Barrel":                              2,
    "Store BookBlo":                             2,
    "Store Fridge":                              2,
    "Store Fridgling":                           2,
    "Store Leeches!":                            2,
    "Store Chairapist":                          2,
    "Store Real Gym":                            2,
    "Store Patrice":                             2,
    "Store Office Chair":                        2,
    "Store Desk":                                2,
    # HEAVY (weight 4) — requires 3 dumbbells
    "Store Windmill":                            3,
    "Store Ougham Stone":                        3,
    "Store Coffee Shop (closed)":                3,
    "Store Police Car":                          3,
    # CHUNKY (weight 5) — requires all 4 dumbbells
    "Store Gym":                                 4,
    "Store Plimbo":                              4,
    "Store Belgium Waffle":                      4,
}


def items(count: int) -> HasFromList:
    """Rule: player has deposited at least `count` collectible items."""
    return HasFromList(*DUMPSTER_ITEMS, count=count)


def set_all_rules(world: FuniRaccoonWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: FuniRaccoonWorld) -> None:
    def rule(name: str, r) -> None:
        world.set_rule(world.get_location(name), r)

    # Victory requires all 3 Progressive Cooling Rods, Orb, Kei Truck, and 50 items received
    rule("Victory", Has("Progressive Cooling Rod", 3) & Has("Orb") & Has("Kei Truck") & items(50))

    # Dumbbell size rules for store locations (TINY items have no requirement)
    for loc_name, count in _DUMBBELL_REQUIREMENTS.items():
        rule(loc_name, Has("Progressive Mystical Dumbbell", count))

    # Within Billdal Mines, Michi and Broken Wall also require the Pickaxe
    rule("Store Michi",       Has("Pickaxe"))
    rule("Store Broken Wall", Has("Pickaxe"))
    rule("Find Michi Cat",    Has("Pickaxe"))

    # Folding Chair requires the Priestess (in addition to the dumbbell weight rule)
    rule("Store Folding Chair", Has("Progressive Mystical Dumbbell", 1) & Has("Priestess"))

    # Blue Mystical Jewel requires 1 dumbbell (found in Howth, Act 2)
    rule("Find Blue Mystical Jewel", Has("Progressive Mystical Dumbbell", 1))

    # Higher Kei Truck scores require at least one truck upgrade
    _truck_upgrade = HasFromList("Kei Truck Boost", "Kei Truck Toaster", count=1)
    for score_check in ("Get 2000 Score with Kei Truck", "Get 3000 Score with Kei Truck",
                        "Get 4000 Score with Kei Truck", "Get 5000 Score with Kei Truck"):
        rule(score_check, _truck_upgrade)


def set_completion_condition(world: FuniRaccoonWorld) -> None:
    world.set_completion_rule(Has("Progressive Cooling Rod", 3) & Has("Orb") & Has("Kei Truck") & items(50))
