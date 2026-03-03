### pull.py
###
### Updates game decompilation projects by performing git pulls in their respective directories
### Usage: python3 pull.py --games="" OR python3 pull.py
import os
import argparse
from pathlib import Path
from _utils import parse_comma_sep, get_project_from_dir

parser = argparse.ArgumentParser(
    description="Checkout the default branch and performs a Git pull on selected decompilation projects"
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

print("You are about to update your project(s). This will checkout to the master/main branch and perform a git pull.")
print("Proceed? (Y/N): ")
proceed = input()

if proceed.lower().startswith('y'):
    if args.games:
        for game in args.games:
            os.system(f"cd /projects/n64/{game}/ && git checkout master || git checkout main && git pull")
    else:
        games_dir = Path("/projects/n64/")
        for dir in games_dir.iterdir():
            if dir.is_dir():
                dir_str = get_project_from_dir(dir)
                print(f"\nPulling {dir_str}\n")
                os.system(f"cd {dir} && git checkout master || git checkout main && git pull")
else:
    print("Cancelling.")
