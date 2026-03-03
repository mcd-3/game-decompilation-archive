### setup.py
###
### Sets up a game decompilation project by copying the base ROM and building
### Usage: python3 setup.py --game="" --version=""
import argparse
from _utils import is_valid_game_and_version
from _setups import paper_mario, sm64, majoras_mask, banjo_kazooie, harvest_moon, perfect_dark, ocarina_of_time, duke_nukem

parser = argparse.ArgumentParser(
    description="Sets up a decompilation project"
)

parser.add_argument(
    "--game",
    "-g",
    type=str,
    default="",
    metavar='GAME',
    help='Specify a game to set up'
)

parser.add_argument(
    "--version",
    "-v",
    type=str,
    default="",
    metavar='VERSION',
    help='Specify a game version to set up'
)

args = parser.parse_args()

if args.game and args.version:
    if is_valid_game_and_version(args.game, args.version):
        if (args.game == "papermario"):
            paper_mario(args.version)
        elif (args.game == "sm64"):
            sm64(args.version)
        elif (args.game == "oot"):
            ocarina_of_time(args.version)
        elif (args.game == "mm"):
            majoras_mask(args.version)
        elif (args.game == "banjo-kazooie"):
            banjo_kazooie(args.version)
        elif (args.game == "hm64-decomp"):
            harvest_moon(args.version)
        elif (args.game == "perfect_dark"):
            perfect_dark(args.version)
        elif (args.game == "DukeNukemZeroHour"):
            duke_nukem(args.version)

        print("Setup is complete. Please verify output for any errors.")
else:
    print("Please specify one game and one version.")