### list.py
###
### Lists all available decompilation projects
### Usage: python3 list.py --games="" OR python3 list.py
import argparse
from _utils import parse_comma_sep, read_data_file

parser = argparse.ArgumentParser(
    description="Lists all supported games and versions"
)

parser.add_argument(
    "--games",
    "-g",
    type=parse_comma_sep,
    default=[],
    metavar='GAMES',
    help='Specify one or multiple game names'
)
args = parser.parse_args()

games_data = read_data_file()

if args.games:
    for game in args.games:
        try:
            print(f"{game}:\n  Versions: {games_data[game]}")
        except:
            print(f"Game \"{game}\" not found")
else:
    print("Available Games")
    print("================")
    for key, value in games_data.items():
        print(f"{key}:\n  Versions: {value}")
