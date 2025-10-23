def player_info():
    while True:
        name = input("player name: ")
        # Ask for confirmation
        confirm = input(f"Are you sure this is your name: '{name}'? (y/n): ").lower()
     return {"name": name, "win": 0, "lose": 0}

def misc():
    player = player_info()
    print(f"Player info: {player}")

def main():
    misc()
    player_info()

main()