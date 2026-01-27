import random
import Rock_Paper_Scissors_Player



class Player:
    def __init__(self):
        self.name="carl"

    def player_choice(self):
        while True:
            choice=input("""Rock,Paper, Scisors
            1)Rock
            2)Paper
            3)Scisors
            """)
            if choice in ("1","2","3","rock","paper", "scisors"):
                self.choice=choice

                return self.choice           
                
            else:
                print("You need to enter a valid answer.")

class Computer:
    def __init__(self):
        pass

    def computer_choice(enter,self):    

        computer=enter[random.randint(1,3)]
        self.computer=computer

        return self.computer

class Combat:
    def __init__(self,player,computer,possibilities):
        self.player=player
        self.computer=computer
        self.possibility=possibilities

    def game_result(self):

        if self.player=="1" or self.player== "rock":
            if self.computer==self.possibility[2]:
                print("You lose")
                return False
            elif self.computer== self.possibility[3]:
                print("You win")
                return True
            else:
                print("Draw")
                return None

        elif self.player=="2" or self.player== "paper":
            if self.computer==self.possibility[3]:
                print("You lose")
                return False
            elif self.computer== self.possibility[1]:
                print("You win")
                return True
            else:
                print("Draw")
                return None

        elif self.player=="3" or self.player== "scisor":
            if self.computer==self.possibility[1]:
                print("You lose")
                return False
            elif self.computer== self.possibility[2]:
                print("You win")
                return True
            else:
                print("Draw")
                return None

class Flow:
    def __init__(self,player_info,enter):
        self.player=player_info
        self.entries=enter

    def number_game(self):
        while True:
            number_of_game=input("How many game do you want to do?  ")
            print()
            try:
                self.number_of_game=int(number_of_game)
                return self.number_of_game
            except:
                print("You must enter a number.")

    def continuer(self):
        print("""Do you want to continue?
        Enter 1 for Yes
        2 for No """)
        continuer=input()
        if continuer=="1":
            return True
        else:
            return False


    def update_player_info(self):
        verify=self.Jeux.game_result()    
        if verify==True:
            self.player["win"]+=1
        elif verify==False:
            self.player["lose"]+=1    
        elif verify==None:
            self.player["drawn"]+=1
        return self.player

    def flow_of_game(self):
        play=Player

        player=play.player_choice(play)
        computer=Computer.computer_choice(self.entries,Computer)
        print("computer choice is",computer)

        self.Jeux=Combat(computer=computer,player=player,possibilities=self.entries)

        print()

        self.update_player_info()


    

    def replay_condition(self):
        games_to_play=self.number_game()
        while True:
            for game in range(games_to_play): 

                self.flow_of_game()

            if self.continuer():
                games_to_play=self.number_game()
            else:
                break




def main():
    entrie={
        1:"Rock",
        2: "Paper",
        3:"Scisors"}
    try:
        with open("Player_info_Save.txt","r") as file:
            pass
    except FileNotFoundError:
        Rock_Paper_Scissors_Player.save_game("New Game")

    player_list=Rock_Paper_Scissors_Player.create_player_list()
    player_info= Rock_Paper_Scissors_Player.player_info()

    Rock_Paper_Scissors_Player.find_the_player(player_info["name"],player_list)

    deroulement=Flow(player_info,entrie)

    deroulement.replay_condition()


    
    print("You have won:",player_info["win"])
    print("You have lost:",player_info["lose"])
    print("You have drawn:",player_info["drawn"])
    Rock_Paper_Scissors_Player.save_game(player_info)

def main2():
    try:
        main()
    except EOFError:
        # Handle piped/redirected input that ends unexpectedly
        print("\nInput ended unexpectedly. Exiting gracefully.")
    except KeyboardInterrupt:
        # Handle user pressing Ctrl+C during interactive runs
        print("\nInterrupted by user. Exiting.")

main2()