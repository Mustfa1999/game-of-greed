from game_of_greed.banker import Banker

class Game:
    def __init__(self, rolls=None):
        self.rolls = rolls
        self.rounds = 0
        self.quited = False
        self.banker = Banker()


    def play(self):
        print("Welcome to Game of Greed")
        answer_1 = input("Wanna play? ")
        
        if answer_1 == "n":
            print("OK. Maybe another time")
            return 0

        else:
            while not self.quited:
                self.rounds += 1
                print(f"Starting round {self.rounds}")

                while True:
                    print("Rolling 6 dice...")

                    # rolled_dice = [str(i) for i in self.rolls(6)]
                    print(','.join(self.rolls(6)))

                    answer_2 = input("Enter dice to keep (no spaces), or (q)uit: ")

                    if answer_2 == "q":
                        print(f"Total score is {self.banker.balance} points")
                        self.quited = True
                        break
                    else:
                        print(answer_2)
                        print("You have 1500 unbanked points and 0 dice remaining")

                        answer_3 = input("(r)oll again, (b)ank your points or (q)uit ")

                        if answer_3 == "r":
                            continue
                        elif answer_3 == "b":
                            print(f"You banked 2400 points in round {self.rounds}")
                            print(f"Total score is {self.banker.balance} points")
                            break
                        else:   # q
                            print(f"Total score is {self.banker.balance} points")
                            self.quited = True
                            break
                            

        print(f"Thanks for playing. You earned {self.banker.balance} points")
                            






if __name__ == "__main__":
    pass

