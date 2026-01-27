class Player:
    def __init__(self):
        pass
    def cool(self):
        self.ask="jjk" 
        print(self.ask)


    def player_choice(self):
        # self.c
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

chrar=Player

chrar.cool(Player)
chrar.player_choice(chrar)



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
            
jeux=Combat("df","fs","ff")
print(type(jeux))