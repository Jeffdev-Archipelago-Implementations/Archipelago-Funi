from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.rules import Has

from .rules import items

if TYPE_CHECKING:
    from .world import FuniRaccoonWorld

# Item-count thresholds that unlock floors/clusters (based on dumpster score):
#   15  - Museum opens
#   25  - Beenie Cluster (Beenie HQ, Goo Office, Parking Lot) unlocks
#   30  - Third floor (act3) opens
#   35  - Blimbo City cluster unlocks (also requires Kei Truck)
#   50  - Post-apocalypse areas (act4) accessible (also requires Kei Truck)
#   100 - Gully Special Island / Belgium Waffle (also requires Kei Truck)

ALL_REGIONS = [
    "Overworld",
    "Chicken Farm",
    "Museum",
    "Beenie Cluster",
    "Underground Metro",
    "Parking Lot",
    "Parking Lot (Truck)",
    "Trasco",
    "Fridge World",
    "Act 3",
    "Blimbo Village",
    "Billdal Mines",
    "Act 3 Blimbo",
    "RBMK",
    "Act 4",
    "Gully Special Island",
]


def create_and_connect_regions(world: FuniRaccoonWorld) -> None:
    regions = {name: Region(name, world.player, world.multiworld) for name in ALL_REGIONS}
    for region in regions.values():
        world.multiworld.regions.append(region)

    def connect(from_name: str, to_name: str, rule=None) -> None:
        world.create_entrance(regions[from_name], regions[to_name], rule)

    # --- Act 1 special ---
    connect("Overworld", "Chicken Farm")

    # --- Museum (15 items) ---
    connect("Overworld", "Museum", items(15))

    # --- Beenie Cluster (act2, 25 items) ---
    # Covers Beenie HQ, Beenie Factory, The Proccess, THE MACHINE,
    # Fish Vore, Fields, Patrick's Secret Place, Goo Office, and Howth
    connect("Overworld", "Beenie Cluster", items(25))

    # Underground Metro only accessible after Beenie is replaced in THE MACHINE
    connect("Beenie Cluster", "Underground Metro")

    # --- Parking Lot (25 items, no truck needed via Goo Office shortcut) ---
    connect("Overworld", "Parking Lot", items(25))
    connect("Parking Lot", "Parking Lot (Truck)", Has("Kei Truck"))
    connect("Parking Lot", "Trasco")
    connect("Trasco", "Fridge World")

    # --- Act 3 (third floor, 30 items) ---
    # Kei Truck is findable in Act 3; Blimbo Village requires the truck
    connect("Overworld", "Act 3", items(30))
    connect("Act 3", "Blimbo Village", Has("Kei Truck"))
    connect("Blimbo Village", "Billdal Mines")

    # --- Act 3 Blimbo / Blimbo City (35 items + Kei Truck) ---
    connect("Overworld", "Act 3 Blimbo", items(35) & Has("Kei Truck"))
    connect("Act 3 Blimbo", "RBMK", Has("Kei Truck"))

    # --- Act 4 (post-apocalypse, 50 items + Kei Truck) ---
    connect("Overworld", "Act 4", items(50) & Has("Kei Truck"))

    # --- Gully Special Island (100 items + Kei Truck) ---
    # This is basically entirely just for the Belgian Waffle lol
    connect("Overworld", "Gully Special Island", items(100) & Has("Kei Truck"))
