from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.rules import Has, HasFromList

from .rules import OutOfLogic, items

if TYPE_CHECKING:
    from .world import FuniRaccoonWorld

# Item-count thresholds that unlock floors/clusters (based on dumpster score):
#   15  - Museum opens
#   25  - Beenie HQ (Act 2 cluster); Trasco Carpark via Goo Office shortcut
#   35  - Driving Test/Blimbo City (Act 3 entry, contains Kei Truck)
#   50  - Post-apocalypse areas (Act 4) accessible (also requires Kei Truck)
#   100 - The Gully accessible (also requires Kei Truck)

ALL_REGIONS = [
    # Act 1 (Norwich/Rackheath starting area)
    "Overworld",
    "Behrman Gymnasium",
    "Behrman Speedway",
    "Tyre World",
    "Chicken Farm",
    "HAT STORE",
    "Cleaners",
    "Da Waaaater Zoooone",
    "Museum",
    "Raccoon Central Station",
    # Act 2 (Beenie cluster)
    "Beenie HQ",
    "Chamber",
    "Beenie Factory",
    "The Process",
    "THE MACHINE",
    "Fish Vore",
    "Goo Office",
    "Underground Metro",
    "Beenies Ascension",
    "Fields",
    "Fellowship",
    "Howth",
    # Act 3
    "Driving Test",
    "Cricket",
    "The Forest",
    "Trasco Carpark",
    "Fridge World",
    "Blimbo Village",
    "Petrol Station",
    "Bildal Mines",
    "Mikk Barge",
    "Garden World",
    "Purgatory",
    # Act 3 Blimbo City cluster
    "Blimbo City",
    "Pub",
    "BLMB Reactor Core",
    # Act 4 (post-apocalypse)
    "Messed Up Canyon",
    "Pharmacy",
    "The Desert",
    "The Well of Knowledge",
    "Cliffs of Nowher",
    "Da Dryyyy Zoooone",
    "Municipal Wastes",
    "The Gully",
]


def create_and_connect_regions(world: FuniRaccoonWorld) -> None:
    regions = {name: Region(name, world.player, world.multiworld) for name in ALL_REGIONS}
    for region in regions.values():
        world.multiworld.regions.append(region)

    def connect(from_name: str, to_name: str, rule=None) -> None:
        world.create_entrance(regions[from_name], regions[to_name], rule)

    # --- Act 1 ---
    connect("Overworld", "Behrman Gymnasium")
    connect("Overworld", "Behrman Speedway", Has("Brob Energy") | OutOfLogic("Speedway accessible without items"))
    connect("Overworld", "Tyre World")
    connect("Overworld", "Chicken Farm", (Has("Brob Energy")) | OutOfLogic("Chicken Farm accessible without items"))
    connect("Overworld", "HAT STORE")
    connect("Overworld", "Cleaners")
    connect("Overworld", "Da Waaaater Zoooone")
    connect("Overworld", "Raccoon Central Station")

    # --- Museum (15 items) ---
    connect("Overworld", "Museum", items(15))
    connect("Museum", "Chamber")

    # --- Act 2 (25 items) — Beenie HQ is the entry hub ---
    connect("Overworld", "Beenie HQ", items(25))
    connect("Beenie HQ", "Beenie Factory", items(25))
    connect("Beenie Factory", "The Process", Has("Goo"))
    connect("The Process", "THE MACHINE", Has("Goo"))
    connect("Beenie HQ", "Fish Vore", items(25))
    connect("The Process", "Goo Office", Has("Goo"))
    connect("THE MACHINE", "Beenies Ascension", Has("Goo"))
    connect("Beenie HQ", "Fields", Has("Goo") | OutOfLogic("Fields accessible without Goo"))
    connect("Overworld", "Fellowship", Has("Goo") & items(25))
    connect("Beenie HQ", "Howth", Has("Goo"))
    connect("Beenie HQ", "Underground Metro", Has("Goo") | OutOfLogic("Underground Metro accessible without Goo"))

    # --- Act 3 (35 items) — Driving Test is the entry, contains Kei Truck ---
    connect("Overworld", "Driving Test", items(35))
    connect("Driving Test", "Blimbo Village", Has("Kei Truck") | OutOfLogic("Blimbo Village accessible without Kei Truck"))
    connect("Blimbo Village", "Cricket")
    connect("Blimbo Village", "The Forest")
    connect("Blimbo Village", "Purgatory")
    connect("Blimbo Village", "Petrol Station")
    connect("Blimbo Village", "Bildal Mines", Has("Old Ass Rusty Ass Key"))
    connect("Bildal Mines", "Garden World", Has("Pickaxe"))
    connect("Bildal Mines", "Mikk Barge", Has("Pickaxe"))
    connect("Blimbo Village", "Trasco Carpark", Has("Kei Truck"))

    # --- Trasco Carpark ---
    connect("Trasco Carpark", "Fridge World", Has("Fridge Key"))

    # --- Blimbo City cluster (35 items + Kei Truck) ---
    connect("Trasco Carpark", "Blimbo City", Has("Kei Truck"))
    connect("Blimbo City", "Pub")
    connect("Blimbo City", "BLMB Reactor Core", Has("Progressive Cooling Rod", 1))

    # --- Act 4 (50 items + Kei Truck) ---
    connect("BLMB Reactor Core", "Messed Up Canyon", items(50) & Has("Progressive Cooling Rod", 1))
    connect("Messed Up Canyon", "Pharmacy")
    connect("Messed Up Canyon", "The Desert")
    connect("Messed Up Canyon", "The Well of Knowledge")
    connect("Messed Up Canyon", "Cliffs of Nowher")
    connect("Messed Up Canyon", "Da Dryyyy Zoooone")
    connect("Messed Up Canyon", "Municipal Wastes")

    # --- The Gully (3 Prog Cooling Rods needed) ---
    connect("Messed Up Canyon", "The Gully", Has("Progressive Cooling Rod", 3) | OutOfLogic("The Gully is accessible with just Kei Truck"))
