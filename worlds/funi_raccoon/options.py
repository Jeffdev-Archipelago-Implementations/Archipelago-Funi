from dataclasses import dataclass

from Options import PerGameCommonOptions, Toggle, DefaultOnToggle, OptionSet, DeathLink, Range

class Goal(OptionSet):
    """
    Select one or more goals you will have to complete to win the run.
    orb: 50 dumpster items, the Orb, 3 Progressive Cooling Rods. Throw the orb in the pot.
    museum: 100 dumpster items, the Belgium Waffle, 4 Progressive Mystical Dumbbells, 3 Progressive Cooling Rods. Throw the Belgium Waffle in the pot.
    fellowship: 50 dumpster items, the GREENISH ABOMINATION, the Priestess, 3 Progressive Cooling Rods. Throw the GREENISH ABOMINATION in the pot.
    lugh: 50 dumpster items, all 4 Mystical Gems. Jump into Lugh's hands in the pot.
    """
    display_name = "Goal"
    valid_keys = ["orb", "museum", "fellowship", "lugh"]
    default = {"orb"}

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


class LughQuestLocking(Toggle):
    """
    When enabled, Lugh will not accept items you bring to him unless you have been sent that specific item.
    """
    display_name = "Lugh Quest Locking"
    
    
class DumpsterWeightBlocking(DefaultOnToggle):
    """
    When enabled (default), the dumpster enforces weight limits strictly: truck weight skips are
    removed from logic entirely and all dumbbell requirements always apply. You will not
    be able to use the truck to store heavier objects.
    When disabled, logic expects you to use the Kei Truck to bypass weight
    requirements in areas where the truck is accessible.
    """
    display_name = "Dumpster Weight Blocking"


class TrapToggle(Toggle):
    """
    When enabled, trap items (Police Trap, Phone Ratio Trap) may appear in the item pool
    as filler, replacing some Euro drops.
    """
    display_name = "Trap Toggle"


class DeathLinkAmnesty(Range):
    """
    Number of deaths to get in your game before a deathlink is sent to another player.
    """
    display_name = "DeathLink Amnesty"
    range_start = 1
    range_end = 10
    default = 1


@dataclass
class FuniRaccoonOptions(PerGameCommonOptions):
    eurosanity: Eurosanity
    gemsanity: Gemsanity
    catsanity: Catsanity
    hatsanity: Hatsanity
    goal: Goal
    dumpster_weight_blocking: DumpsterWeightBlocking
    lugh_quest_locking: LughQuestLocking
    trap_toggle: TrapToggle
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty
