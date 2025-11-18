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

'''
def new_save(player):
    with open("Player_info_Save.txt","w") as file: 
        for element in player:
            file.write("\n")       
            file.write(f"{element}")
'''        

def save_game(player):
    with open("Player_info_Save.txt","a") as file: 
        file.write("\n")
        for element in player:       
            file.write(f"{element} ")



def create_player_list():
    new_list=[]
    with open("Player_info_Save.txt","r") as file:
        for line in file:
            new_list.append(line)
    return new_list


new_list=create_player_list()

def find_the_player(player,new_list):
    for elements in new_list:
        if player in elements:
            #print(elements, new_list.index(elements))
            saved_player_info=elements
            return saved_player_info

    


# j=str(find_the_player("josh",new_list))


# l=str({'name': 'josh', 'win': 0, 'lose': 0, 'drawn': 0})
k={'name': 'josh', 'win': 0, 'lose': 0, 'drawn': 0}


# print(type(j))

# h=str({'name': 'josh', 'win': 0, 'lose': 0, 'drawn': 0})
# print(h)

# if j==k:
#     print("g")
# else:
#     print("d")

# mj="{'name': 'josh', 'win': 0, 'lose': 0, 'drawn': 0}"

# if l==k:
#     print("Gsh")


j="['sdfgd', 13, 14, 22]"
h=j.split()
# print(h,type(h))
# print(type(h[1]))
# int(h[1])
# m=k.values()

# g=list(m)
# print(g)
l=find_the_player("fsf",new_list)

print(type(l))