from dataclasses import dataclass

from Options import PerGameCommonOptions, Toggle, DefaultOnToggle, Choice

class Goal(Choice):
    """
    Set the specified goal you want to have to get for goaling the Archipelago.
    Orb: The orb ending, achieved by getting 50 dumpster items, the orb, 3 progressive cooling rods, and the kei truck. (default)
    Museum: The museum ending, achieved by getting 100 dumpster items, the belgium waffle, 3 progressive cooling rods, and the kei truck.
    Fellowship: The fellowship ending, achieved by getting 25 dumpster items, the priestess, and the GREENISH ABOMINATION.
    Lugh: The Lugh ending, achieved by getting 50 dumpster items, all 4 mystical jewels, the kei truck, and the unregistered firearm.
    """
    display_name = "Goal"
    option_orb = 0
    option_museum = 1
    option_fellowship = 2
    option_lugh = 3

class Eurosanity(Toggle):
    """
    Include the scattered Euro collectibles as randomizer locations.
    """
    display_name = "Eurosanity"


class Gemsanity(DefaultOnToggle):
    """
    Include the Mystical Gem locations as randomizer checks.
    Automatically enabled if is the Lugh goal is selected.
    """
    display_name = "Gemsanity"


class Catsanity(DefaultOnToggle):
    """
    Include the Find Cat locations as randomizer checks.
    Storing cats at the dumpster is always included.
    """
    display_name = "Catsanity"


class Hatsanity(DefaultOnToggle):
    """
    Include the hat locations as randomizer checks.
    """
    display_name = "Hatsanity"


@dataclass
class FuniRaccoonOptions(PerGameCommonOptions):
    eurosanity: Eurosanity
    gemsanity: Gemsanity
    catsanity: Catsanity
    hatsanity: Hatsanity
    goal: Goal
