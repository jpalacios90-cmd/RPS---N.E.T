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

    return {"name": name, "win": 0, "lose": 0,"drawn":0}




def save_game(player):
    with open("Player_info_Save.txt","a") as file:        
        file.write(f"{player}")
        file.write("\n")
        # file.seek(1000)


    with open("Player_info_Save.txt","r") as file:
        redact=file.read()
        return redact




def t():
    files=save_game()

    print(files)



    if "irt" in files:
        print("gotcha")
    else:
        print("missing")
