Rock_Paper_Scissors.py
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

    return {"name": name, "win": 0, "lose": 0}

def main():
    player = player_info()
    print(f"Player info: {player}")

main()
