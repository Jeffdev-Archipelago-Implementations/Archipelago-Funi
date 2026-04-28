from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import FuniRaccoonWorld

LOCATION_NAME_TO_ID = {
    "Store Moai": 1001,
    "Store Street Lamp": 1002,
    "Store Funbells": 1003,
    "Store Lama/Alpaca Maybe?": 1004,
    "Store Gym": 1005,
    "Store Kei Truck": 1006,
    "Store Vending Machine (accepts doubloons)": 1007,
    "Store DOUBLOONS": 1008,
    "Store Radio": 1009,
    "Store unregistered firearm": 1011,
    "Store Under Construction": 1016,
    "Store Chicken": 1017,
    "Store Washing Machine": 1018,
    "Store Michelle": 1019,
    "Store Brob Energy": 1020,
    "Store Buisness Man": 1021,
    "Store Concrete": 1022,
    "Store Gizmo": 1023,
    "Store Keksz": 1024,
    "Store Michi": 1025,
    "Store boingler": 1026,
    "Store Paracetamol 650mg": 1027,
    "Store Heavy Stone Torch": 1028,
    "Store Computer Monitor (60hz)": 1031,
    "Store Sign": 1037,
    "Store Crack Head": 1038,
    "Store Crayon": 1039,
    "Store Cricket Bat": 1040,
    "Store Pirate": 1042,
    "Store Pirate 2": 1043,
    "Store Pirate 3": 1044,
    "Store ROAD NOT DONE": 1045,
    "Store Microwave": 1048,
    "Store Toaster": 1049,
    "Store Logan Left": 1050,
    "Store Logan Right": 1051,
    "Store Evil Fish": 1052,
    "Store Feral Dog": 1053,
    "Store Windmill": 1054,
    "Store Marketable Plushie Box": 1055,
    "Store Goo": 1056,
    "Store Beenie the Birthday Boy": 1057,
    "Store Fan": 1059,
    "Store Letter B": 1061,
    "Store Beenie, Our Savior": 1062,
    "Store Candle": 1063,
    "Store Funi Marketable Plushie": 1064,
    "Store Patrick O'Hara": 1065,
    "Store Toastie": 1066,
    "Store Crisp": 1067,
    "Store Flower": 1068,
    "Store Divider": 1069,
    "Store Office Chair": 1070,
    "Store Desk": 1071,
    "Store My Favourite Chair": 1073,
    "Store Cricket": 1074,
    "Store Crisps Undying Love": 1075,
    "Store Blimbo Village Sign": 1076,
    "Store Ougham Stone": 1077,
    'Store "Cow"': 1078,
    "Store Old Ass Rusty Ass Key": 1080,
    "Store Plimbo": 1081,
    "Store Fridge Key": 1082,
    "Store Orphan Tyre": 1084,
    "Store Papa Tyre": 1085,
    "Store Smoker": 1086,
    "Store Broken Truck": 1087,
    "Store CHEESE": 1088,
    "Store Gas Drum": 1089,
    "Store Coffee Shop (closed)": 1090,
    "Store Trolley": 1091,
    "Store Folding Chair": 1093,
    "Store Cooling Rod": 1094,
    "Store Warning": 1095,
    "Store Pickaxe": 1096,
    "Store Broken Wall": 1097,
    "Store Fone": 1098,
    "Store Coffee Cup": 1099,
    "Store Kettle": 1100,
    "Store Radiator": 1101,
    "Store Flower Blimbo": 1102,
    "Store Bench": 1104,
    "Store Evil Raccoon": 1105,
    "Store Naked Fella": 1106,
    "Store Bin": 1107,
    "Store Knifedog": 1109,
    "Store Suitcase": 1110,
    "Store Cheeky Pint": 1111,
    "Store Flowian": 1112,
    "Store Bomb": 1113,
    "Store Bell Boy": 1114,
    "Store Demon Core": 1115,
    "Store Apple": 1116,
    "Store Gas Pumpo": 1117,
    "Store CD Player": 1118,
    "Store Radio Blimbo": 1119,
    "Store Binocublo": 1120,
    "Store Police Car": 1121,
    "Store Hazelnut": 1122,
    "Store Anti Sads": 1123,
    'Store "TV Remote"': 1124,
    "Store Synthesizer": 1125,
    "Store Brick": 1126,
    "Store Lloyd": 1127,
    "Store Manhole Cover": 1128,
    "Store Old Sign": 1129,
    "Store Warning Sign": 1130,
    "Store Area Sign": 1131,
    "Store Orb": 1132,
    "Store Ms. Heel": 1134,
    "Store Mr. Heel": 1135,
    "Store Belgium Waffle": 1136,
    "Store GREENISH ABOMINATION": 1137,
    "Store Priestess": 1138,
    "Store Beenie Saves The Orphans": 1140,
    "Store Eel Can": 1141,
    "Store Barrel": 1142,
    "Store BookBlo": 1143,
    "Store Fridge": 1144,
    "Store Fridgling": 1145,
    "Store Snowball": 1146,
    "Store Leeches!": 1147,
    "Store Plimbo's Cooling Rod": 1148,
    "Store Fridge King's Cooling Rod": 1149,
    "Store Beach Ball": 1150,
    "Store Milk Klubnika": 1151,
    "Store Chairapist": 1154,
    "Store Digital Polaroid Camera": 1155,
    "Store Yolky": 1156,
    "Store Pawn": 1157,
    "Store Rook": 1158,
    "Store Bishop": 1159,
    "Store Queen": 1160,
    "Store King": 1161,
    "Store Real Gym": 1162,
    "Store Spoonsweet": 1163,
    "Store Wriks Celler": 1164,
    "Store Door": 1165,
    "Store Funi Raccoon Game Deluxe": 1166,
    "Store Patrice": 1167,
    "Store Goo Container": 1168,
    "Store Butterfly": 1169,
    "Store Patrick O Bobble": 1170,
    "Store Dice": 1171,
    "Store Lughling": 1172,
    "Store Book Stack": 1173,
    "Store Average Canadian": 1174,
    "Store Cheese Wife": 1175,
    "Get 1000 Score with Kei Truck": 2001,
    "Get 2000 Score with Kei Truck": 2002,
    "Get 3000 Score with Kei Truck": 2003,
    "Get 4000 Score with Kei Truck": 2004,
    "Get 5000 Score with Kei Truck": 2005,
    "Eat Mystical Dumbbell 1": 3001,
    "Eat Mystical Dumbbell 2": 3002,
    "Eat Mystical Dumbbell 3": 3003,
    "Eat Mystical Dumbbell 4": 3004,
    "Purchase Kei Truck Radio":   4001,
    "Purchase Kei Truck Toaster": 4002,
    "Purchase Kei Truck Boost":   4003,
    "Find Michi Cat": 5001,
    "Find Michelle Cat": 5002,
    "Find Concrete Cat": 5003,
    "Find Gizmo Cat": 5004,
    "Find Keksz Cat": 5005,
    "Find boingler Cat": 5006,
    "Find Sun Hat":          6001,
    "Find Sombrero":         6002,
    "Find Top Hat":          6003,
    "Find Jester Hat":       6004,
    "Find Raccoon Hat":      6005,
    "Find Media Player Hat": 6006,
    "Find Fridge Crown":     6007,
    "Find Patty Hat":        6008,
    "Eat Green Mystical Gem":  7001,
    "Eat Blue Mystical Gem":   7002,
    "Eat Purple Mystical Gem": 7003,
    "Eat Red Mystical Gem":    7004,
    
    # --- Euro collectibles ---
    "Norwich: Euro at train station":               8001,
    "Norwich: Euro at chicken farm island":         8002,
    "Chicken Farm: Euro on pillar":                 8003,
    "Gym: Euro on roof with vending machine":       8004,
    "Gym: Euro behind building":                    8005,
    "Gym: Euro at end of train tracks":             8006,
    "Gym: Euro on bee sign under clouds":           8007,
    "Tyre: Euro on roof of entrance":               8008,
    "Water Zone: Euro under stairs underwater":     8009,
    "Beenie Death: Euro behind cross":              8010,
    "Canyon: Euro on edge of canyon":               8011,
    "Trasco: Euro on edge wall 1":                  8012,
    "Trasco: Euro on edge wall 2":                  8013,
    "Trasco: Euro on edge wall 3":                  8014,
    "City: Euro on watertower":                     8015,
    "City: Euro near boat on edge of city":         8016,
    "City: Euro at Robin P. Bobin Store":           8017,
    "City: Euro next to Robin P. Bobin Store":      8018,
    "City: Euro near Guns stands":                  8019,
    "City: Euro under city on girders 1":           8020,
    "City: Euro under city on girders 2":           8021,
    "City: Euro under city on girders 3":           8022,
    "City: Euro under city on girders 4":           8023,
    "City: Euro near cheese wheel":                 8024,
    "Village: Euro on castle":                      8025,
    "Village: Euro near furnace":                   8026,
    "Wastes: Euro on top of breakfast building":    8027,
    "Wastes: Euro on top of chinese building":      8028,
    "Wastes: Euro on lower end of chinese building": 8029,
    "Wastes: Euro on sad therapy sign building":    8030,
    "Wastes: Euro nearby mystical dumbbell in flowers": 8031,
    "Wastes: Euro on road edge":                    8032,
    "Wastes: Euro on dead blimbos building":        8033,
    "Desert: Euro on tilted building":              8034,
    "Desert: Euro in moai head pool 1":             8035,
    "Desert: Euro in moai head pool 2":             8036,
    "Desert: Euro in moai head pool 3":             8037,
    "Desert: Euro in moai head pool 4":             8038,
    "Desert: Euro in moai head pool 5":             8039,
    "Desert: Euro in moai head pool 6":             8040,
    "Desert: Euro on pillar near MFC":              8041,
    "Desert: Euro on yellow house roof in fridge land": 8042,
    "Desert: Euro in New Buisness HQ":              8043,
    "Desert: Euro on top of fridge land skull":     8044,
    "Desert: Euro on blue house roof in fridge land": 8045,
    "Desert: Euro in BLMB nuclear reactor":         8046,
}


class FuniRaccoonLocation(Location):
    game = "Funi Raccoon Game"


# Maps each location to the region it belongs in. Anything not listed defaults to Overworld.
LOCATION_REGION: dict[str, str] = {
    # --- Chicken Farm ---
    "Store Chicken": "Chicken Farm",

    # --- Museum (3 items) ---
    "Store Spoonsweet":     "Museum",
    "Store Wriks Celler":   "Museum",
    "Store Logan Left":     "Museum",   # also Beenie HQ; Museum is earlier
    "Store Logan Right":    "Museum",
    "Store Pawn":           "Museum",   # also Garden World; Museum is earlier
    "Store Rook":           "Museum",
    "Store Bishop":         "Museum",
    "Store King":           "Museum",
    "Store Queen":          "Museum",
    "Store Barrel":         "Museum",   # also Blimbo Forest / Canyon; Museum is earlier

    # --- Beenie Cluster (act2, 25 items) ---
    # Beenie HQ, Beenie Factory, The Proccess, THE MACHINE,
    # Fish Vore, Fields, Patrick's Secret Place, Goo Office, Howth
    "Store Buisness Man":               "Beenie Cluster",
    "Store Pirate":                     "Beenie Cluster",
    "Store Pirate 2":                   "Beenie Cluster",
    "Store Pirate 3":                   "Beenie Cluster",
    "Store Microwave":                  "Beenie Cluster",
    "Store Evil Fish":                  "Beenie Cluster",
    "Store Feral Dog":                  "Beenie Cluster",
    "Store Windmill":                   "Beenie Cluster",
    "Store Marketable Plushie Box":     "Beenie Cluster",
    "Store Goo":                        "Beenie Cluster",
    "Store Beenie the Birthday Boy":    "Beenie Cluster",
    "Store Letter B":                   "Beenie Cluster",
    "Store Candle":                     "Beenie Cluster",
    "Store Funi Marketable Plushie":    "Beenie Cluster",
    "Store Patrick O'Hara":             "Beenie Cluster",
    "Store Crisp":                      "Beenie Cluster",
    "Store Flower":                     "Beenie Cluster",
    "Store Divider":                    "Beenie Cluster",
    "Store Office Chair":               "Beenie Cluster",
    "Store Desk":                       "Beenie Cluster",
    "Store Beach Ball":                 "Beenie Cluster",
    "Store Beenie Saves The Orphans":   "Beenie Cluster",
    "Store Plimbo":                     "Beenie Cluster",
    "Store Goo Container":              "Beenie Cluster",
    "Store Kettle":                     "Beenie Cluster",   # via Howth
    "Store Street Lamp":                "Beenie Cluster",   # via Howth / Parking Lot

    # --- Underground Metro (Funi Marketable Plushie, within Beenie Cluster) ---
    "Store Keksz": "Underground Metro",
    "Find Keksz Cat": "Underground Metro",

    # --- Parking Lot (25 items, no truck, via Goo Office shortcut) ---
    "Store Ougham Stone":           "Parking Lot",
    "Store Coffee Shop (closed)":   "Parking Lot",
    "Store Trolley":                "Parking Lot",
    "Store Fridge Key":             "Parking Lot",
    "Store CHEESE":                 "Parking Lot",

    # --- Parking Lot (Truck) ---
    "Store CD Player":                  "Parking Lot (Truck)",
    "Store Patrice":                    "Parking Lot (Truck)",
    "Get 1000 Score with Kei Truck":    "Parking Lot (Truck)",
    "Get 2000 Score with Kei Truck":    "Parking Lot (Truck)",
    "Get 3000 Score with Kei Truck":    "Parking Lot (Truck)",
    "Get 4000 Score with Kei Truck":    "Parking Lot (Truck)",
    "Get 5000 Score with Kei Truck":    "Parking Lot (Truck)",
    "Purchase Kei Truck Radio":         "Parking Lot (Truck)",
    "Purchase Kei Truck Toaster":       "Parking Lot (Truck)",
    "Purchase Kei Truck Boost":         "Parking Lot (Truck)",

    # --- Trasco ---
    "Store Fridge": "Trasco",

    # --- Fridge World ---
    "Store Milk Klubnika":             "Fridge World",
    "Store Fridge King's Cooling Rod": "Fridge World",

    # --- Act 3 (third floor, 30 items) — Kei Truck findable here ---
    "Store Kei Truck": "Act 3",

    # --- Blimbo Village (within Act 3, requires Kei Truck) ---
    "Store Cricket Bat":            "Blimbo Village",
    "Store Cricket":                "Blimbo Village",
    "Store Blimbo Village Sign":    "Blimbo Village",
    'Store "Cow"':                  "Blimbo Village",
    "Store Old Ass Rusty Ass Key":  "Blimbo Village",
    "Store Gas Drum":               "Blimbo Village",
    "Store Flowian":                "Blimbo Village",
    "Store Eel Can":                "Blimbo Village",
    "Store Binocublo":              "Blimbo Village",
    "Store Gas Pumpo":              "Blimbo Village",
    "Store Police Car":             "Blimbo Village",
    "Store Bomb":                   "Blimbo Village",
    "Store Knifedog":               "Blimbo Village",
    "Store Radio Blimbo":           "Blimbo Village",
    "Store Fone":                   "Blimbo Village",
    "Store Door":                   "Blimbo Village",
    "Store UNDER CONSTRUCTION":     "Blimbo Village",
    "Store Under Construction":     "Blimbo Village",
    "Purchase Kei Truck Radio":     "Blimbo Village",
    "Purchase Kei Truck Boost":     "Blimbo Village",
    "Purchase Kei Truck Toaster":   "Blimbo Village",

    # --- Billdal Mines (Old Ass Rusty Ass Key, within Blimbo Village) ---
    "Store Pickaxe":               "Billdal Mines",
    "Store boingler":              "Billdal Mines",
    "Find boingler Cat":           "Billdal Mines",
    "Store Broken Wall":           "Billdal Mines",  # also needs Pickaxe (location rule in rules.py)
    "Store Michi":                 "Billdal Mines",  # also needs Pickaxe (location rule in rules.py)
    "Find Michi Cat":              "Billdal Mines",  # also needs Pickaxe (location rule in rules.py)
    "Store Plimbo's Cooling Rod":  "Billdal Mines",

    # --- Act 3 Blimbo (35 items) ---
    "Store Coffee Cup":         "Act 3 Blimbo",
    "Store Evil Raccoon":       "Act 3 Blimbo",
    "Store Naked Fella":        "Act 3 Blimbo",
    "Store Bin":                "Act 3 Blimbo",
    "Store Suitcase":           "Act 3 Blimbo",
    "Store Bell Boy":           "Act 3 Blimbo",
    "Store Yolky":              "Act 3 Blimbo",
    "Store Crayon":             "Act 3 Blimbo",
    "Store Dice":               "Act 3 Blimbo",
    "Store Average Canadian":   "Act 3 Blimbo",
    "Store Patrick O Bobble":   "Act 3 Blimbo",
    "Store Cheeky Pint":        "Act 3 Blimbo",   # Pub, connected from Blimbo City
    "Store Radiator":           "Act 3 Blimbo",

    # --- RBMK (Kei Truck, within Act 3 Blimbo) ---
    "Store Warning":      "RBMK",
    "Store Demon Core":   "RBMK",
    "Store Cooling Rod":  "RBMK",

    # --- Act 4 (post-apocalypse, 50 items) ---
    "Store Anti Sads":      "Act 4",
    "Store Leeches!":       "Act 4",
    "Store Hazelnut":       "Act 4",
    "Store BookBlo":        "Act 4",
    "Store Cheese Wife":    "Act 4",
    "Store Snowball":       "Act 4",
    "Store Fridgling":      "Act 4",
    "Store Chairapist":     "Act 4",
    "Store Synthesizer":    "Act 4",
    "Store Real Gym":       "Act 4",
    "Store Butterfly":      "Act 4",
    "Store Lughling":               "Act 4",
    "Store Orb":                    "Act 4",
    "Store Funi Raccoon Game Deluxe": "Act 4",

    # --- Gully Special Island (100 items) ---
    "Store Belgium Waffle": "Gully Special Island",

    # --- Mystical Dumbbells ---
    "Eat Mystical Dumbbell 2": "Museum",    # Beenie Museum, Act 2
    "Eat Mystical Dumbbell 3": "Trasco",    # Trasco parking lot, Act 3
    "Eat Mystical Dumbbell 4": "Act 4",     # Municipal Wastes

    # --- Hats ---
    # Sun Hat is in Norwich / Act 1 (Overworld, default — no entry needed)
    "Find Sombrero":         "Chicken Farm",
    "Find Top Hat":          "Museum",
    "Find Jester Hat":       "Beenie Cluster",   # The Process
    "Find Raccoon Hat":      "Blimbo Village",
    "Find Media Player Hat": "Blimbo Village",
    "Find Fridge Crown":     "Act 4",
    "Find Patty Hat":        "Act 3 Blimbo",     # Blimbo City

    # --- Mystical Gems ---
    # Green Jewel is in Da Water Zone / Act 1 (Overworld, default — no entry needed)
    "Eat Blue Mystical Gem":   "Beenie Cluster",   # Howth (rule in rules.py)
    "Eat Purple Mystical Gem": "Blimbo Village",
    "Eat Red Mystical Gem":    "Act 4",

    # --- Euro collectibles ---
    # Norwich and Gym/Tyre/Water Zone are Act 1 (Overworld, default — no entry needed)
    "Chicken Farm: Euro on pillar":                     "Chicken Farm",
    "Beenie Death: Euro behind cross":                  "Beenie Cluster",
    "Trasco: Euro on edge wall 1":                      "Trasco",
    "Trasco: Euro on edge wall 2":                      "Trasco",
    "Trasco: Euro on edge wall 3":                      "Trasco",
    "City: Euro on watertower":                         "Act 3 Blimbo",
    "City: Euro near boat on edge of city":             "Act 3 Blimbo",
    "City: Euro at Robin P. Bobin Store":               "Act 3 Blimbo",
    "City: Euro next to Robin P. Bobin Store":          "Act 3 Blimbo",
    "City: Euro near Guns stands":                      "Act 3 Blimbo",
    "City: Euro under city on girders 1":               "Act 3 Blimbo",
    "City: Euro under city on girders 2":               "Act 3 Blimbo",
    "City: Euro under city on girders 3":               "Act 3 Blimbo",
    "City: Euro under city on girders 4":               "Act 3 Blimbo",
    "City: Euro near cheese wheel":                     "Act 3 Blimbo",
    "Village: Euro on castle":                          "Blimbo Village",
    "Village: Euro near furnace":                       "Blimbo Village",
    "Canyon: Euro on edge of canyon":                   "Act 4",
    "Wastes: Euro on top of breakfast building":        "Act 4",
    "Wastes: Euro on top of chinese building":          "Act 4",
    "Wastes: Euro on lower end of chinese building":    "Act 4",
    "Wastes: Euro on sad therapy sign building":        "Act 4",
    "Wastes: Euro nearby mystical dumbbell in flowers": "Act 4",
    "Wastes: Euro on road edge":                        "Act 4",
    "Wastes: Euro on dead blimbos building":            "Act 4",
    "Desert: Euro on tilted building":                  "Act 4",
    "Desert: Euro in moai head pool 1":                 "Act 4",
    "Desert: Euro in moai head pool 2":                 "Act 4",
    "Desert: Euro in moai head pool 3":                 "Act 4",
    "Desert: Euro in moai head pool 4":                 "Act 4",
    "Desert: Euro in moai head pool 5":                 "Act 4",
    "Desert: Euro in moai head pool 6":                 "Act 4",
    "Desert: Euro on pillar near MFC":                  "Act 4",
    "Desert: Euro on yellow house roof in fridge land": "Act 4",
    "Desert: Euro in New Buisness HQ":                  "Act 4",
    "Desert: Euro on top of fridge land skull":         "Act 4",
    "Desert: Euro on blue house roof in fridge land":   "Act 4",
    "Desert: Euro in BLMB nuclear reactor":             "Act 4",
}


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


_EURO_LOCATIONS  = {n for n, i in LOCATION_NAME_TO_ID.items() if 8001 <= i <= 8999}
_GEM_LOCATIONS   = {n for n, i in LOCATION_NAME_TO_ID.items() if 7001 <= i <= 7999}
_CAT_LOCATIONS   = {n for n, i in LOCATION_NAME_TO_ID.items() if 5001 <= i <= 5999}
_HAT_LOCATIONS   = {n for n, i in LOCATION_NAME_TO_ID.items() if 6001 <= i <= 6999}


def get_excluded_locations(world: FuniRaccoonWorld) -> set[str]:
    excluded: set[str] = set()
    if not world.options.eurosanity:
        excluded |= _EURO_LOCATIONS
    if not world.options.gemsanity:
        excluded |= _GEM_LOCATIONS
    if not world.options.catsanity:
        excluded |= _CAT_LOCATIONS
    if not world.options.hatsanity:
        excluded |= _HAT_LOCATIONS
    return excluded


def create_all_locations(world: FuniRaccoonWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: FuniRaccoonWorld) -> None:
    excluded = get_excluded_locations(world)
    for loc_name, loc_id in LOCATION_NAME_TO_ID.items():
        if loc_name in excluded:
            continue
        region_name = LOCATION_REGION.get(loc_name, "Overworld")
        region = world.get_region(region_name)
        region.add_locations({loc_name: loc_id}, FuniRaccoonLocation)


def create_events(world: FuniRaccoonWorld) -> None:
    overworld = world.get_region("Overworld")
    overworld.add_event(
        "Victory", "Victory", location_type=FuniRaccoonLocation, item_type=items.FuniRaccoonItem
    )
