import json
from pathlib import Path

def parse_comma_sep(s):
    """Converts a comma-separated string to a list of strings, stripping whitespace."""
    if not s:
        return []
    return [item.strip() for item in s.split(',')]

def get_project_from_dir(dir: Path):
    """Gets the project name from a directory path"""
    return dir.absolute().as_posix().split('/').pop()

def read_data_file():
    try:
        with open('/scripts/_games.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: The file '_games.json' was not found.")
        return False
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return False
    
def is_valid_game_and_version(game, version):
    data = read_data_file()
    if game not in data:
        print(f"Game \"{game}\" does not exist")
        return False
    if not data[game]:
        print(f"Game \"{game}\" is not supported")
        return False
    if not version in data[game]:
        print(f"Version \"{version}\" for game \"{game}\" is not supported")
        return False
    return True