import json
from pathlib import Path


HIGHSCORE_FILE = Path(__file__).resolve().parent / "highscore.json"


def load_highscores():
    """Load highscores from disk. Returns a dict of name->wins."""
    if HIGHSCORE_FILE.exists():
        try:
            return json.loads(HIGHSCORE_FILE.read_text(encoding="utf-8"))
        except Exception:
            # Corrupt file or decode error: return empty and overwrite on next save
            return {}
    return {}


def save_highscores(data):
    """Save highscores dict to disk."""
    HIGHSCORE_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def update_highscore(name, wins):
    """Update the stored highscore for `name` if `wins` is higher.

    Returns a tuple (previous_highscore, updated_bool).
    """
    data = load_highscores()
    prev = data.get(name, 0)
    if wins > prev:
        data[name] = wins
        save_highscores(data)
        return prev, True
    return prev, False


def get_highscore(name):
    """Return the stored highscore for `name` (0 if none)."""
    return load_highscores().get(name, 0)


def player_info():
    while True:
        name = input("player name: ").strip()
        # Ask for confirmation
        confirm = input(f"Are you sure this is your name: '{name}'? (y/n): ").strip().lower()
        if confirm in ("y", "yes"):
            break
        elif confirm in ("n", "no"):
            print("Okay, let's try again.")
        else:
            print("Please answer 'y' or 'n'.")
        print()

    return {"name": name, "win": 0, "lose": 0, "drawn": 0}


def player_highscore():
    while True:
        name = input("Enter the name to check highscore: ").strip()
        if name:
            return name
        else:
            print("Name cannot be empty. Please try again.")
