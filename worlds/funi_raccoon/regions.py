from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import FuniRaccoonWorld


def create_and_connect_regions(world: FuniRaccoonWorld) -> None:
    overworld = Region("Overworld", world.player, world.multiworld)
    world.multiworld.regions.append(overworld)
