from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.rules import Has

from .rules import items

if TYPE_CHECKING:
    from .world import FuniRaccoonWorld

# Item-count thresholds that unlock floors/clusters (based on dumpster score):
#   15  - Museum opens
#   25  - Beenie HQ (Act 2 cluster); Trasco Carpark via Goo Office shortcut
#   35  - Driving Test/Blimbo City (Act 3 entry, contains Kei Truck)
#   50  - Post-apocalypse areas (Act 4) accessible (also requires Kei Truck)
#   100 - The Gully accessible (also requires Kei Truck)

ALL_REGIONS = [
    # Act 1 (Norwich starting area)
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
    "Garden World",
    "The Forest",
    "Trasco Carpark",
    "Trasco Carpark (Truck)",
    "Trasco",
    "Fridge World",
    "Blimbo Village",
    "Petrol Station",
    "Bildal Mines",
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
    connect("Overworld", "Behrman Speedway", Has("Vending Machine (accepts doubloons)") & Has("Brob Energy") & Has("Progressive Mystical Dumbbell", 4))
    connect("Overworld", "Tyre World")
    connect("Overworld", "Chicken Farm", Has("Vending Machine (accepts doubloons)") & Has("Brob Energy"))
    connect("Overworld", "HAT STORE")
    connect("Overworld", "Cleaners")
    connect("Overworld", "Da Waaaater Zoooone", Has("unregistered firearm"))
    connect("Overworld", "Raccoon Central Station")

    # --- Museum (15 items) ---
    connect("Overworld", "Museum", items(15))

    # --- Act 2 (25 items) — Beenie HQ is the entry hub ---
    connect("Overworld", "Beenie HQ", items(25))
    connect("Beenie HQ", "Chamber")
    connect("Beenie HQ", "Beenie Factory")
    connect("Beenie HQ", "The Process", Has("Goo"))
    connect("Beenie HQ", "THE MACHINE", Has("Goo"))
    connect("Beenie HQ", "Fish Vore")
    connect("Beenie HQ", "Goo Office", Has("Goo"))
    connect("Beenie HQ", "Beenies Ascension")
    connect("Beenie HQ", "Fields")
    connect("Beenie HQ", "Fellowship", Has("Priestess"))
    connect("Beenie HQ", "Howth", Has("Funi Marketable Plushie"))
    # Underground Metro opens after THE MACHINE
    connect("THE MACHINE", "Underground Metro")

    # --- Trasco Carpark via Goo Office shortcut (25 items, no truck needed) ---
    connect("Goo Office", "Trasco Carpark")
    connect("Trasco Carpark", "Trasco Carpark (Truck)", Has("Kei Truck"))
    connect("Trasco Carpark", "Trasco")
    connect("Trasco", "Fridge World", Has("Fridge Key"))

    # --- Act 3 (35 items) — Driving Test is the entry, contains Kei Truck ---
    connect("Overworld", "Driving Test", items(35))
    connect("Driving Test", "Blimbo Village", Has("Kei Truck"))
    connect("Blimbo Village", "Cricket")
    connect("Blimbo Village", "Garden World", Has("Pickaxe"))
    connect("Blimbo Village", "The Forest")
    connect("Blimbo Village", "Purgatory")
    connect("Blimbo Village", "Trasco Carpark")  # also reachable from Act 3
    connect("Blimbo Village", "Petrol Station")
    connect("Blimbo Village", "Bildal Mines", Has("Old Ass Rusty Ass Key"))

    # --- Blimbo City cluster (35 items + Kei Truck) ---
    connect("Overworld", "Blimbo City", items(35) & Has("Kei Truck"))
    connect("Blimbo City", "Pub")
    connect("Blimbo City", "BLMB Reactor Core", Has("Kei Truck"))

    # --- Act 4 (50 items + Kei Truck) ---
    connect("Overworld", "Messed Up Canyon", items(50) & Has("Kei Truck"))
    connect("Messed Up Canyon", "Pharmacy")
    connect("Messed Up Canyon", "The Desert")
    connect("Messed Up Canyon", "The Well of Knowledge")
    connect("Messed Up Canyon", "Cliffs of Nowher")
    connect("Messed Up Canyon", "Da Dryyyy Zoooone", Has("Anti Sads"))
    connect("Messed Up Canyon", "Municipal Wastes")

    # --- The Gully (100 items + Kei Truck) ---
    connect("Overworld", "The Gully", items(100) & Has("Kei Truck") & Has("Progressive Cooling Rod", 3))
