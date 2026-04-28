from dataclasses import dataclass

from Options import PerGameCommonOptions, Toggle, DefaultOnToggle


class Eurosanity(Toggle):
    """Include the scattered Euro collectibles as randomizer locations."""
    display_name = "Eurosanity"


class Gemsanity(DefaultOnToggle):
    """Include the Mystical Gem locations as randomizer checks."""
    display_name = "Gemsanity"


class Catsanity(DefaultOnToggle):
    """Include the Find Cat locations as randomizer checks.
    Storing cats at the dumpster is always included."""
    display_name = "Catsanity"


class Hatsanity(DefaultOnToggle):
    """Include the hat locations as randomizer checks."""
    display_name = "Hatsanity"


@dataclass
class FuniRaccoonOptions(PerGameCommonOptions):
    eurosanity: Eurosanity
    gemsanity: Gemsanity
    catsanity: Catsanity
    hatsanity: Hatsanity
