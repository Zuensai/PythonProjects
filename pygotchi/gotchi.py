# **************************************************************************** #
#                               _____      ____       _                        #
#                              / ___/     / __ \_____(_)___  ________          #
#                              \__ \     / /_/ / ___/ / __ \/ ___/ _ \         #
#     Author: Sven            ___/ /    / ____/ /  / / / / / /__/  __/         #
#     Created: 2025-11-27    /____(_)  /_/   /_/  /_/_/ /_/\___/\___/          #
#     gotchi.py                                                                #
#                                                                              #
# **************************************************************************** #

class Gotchi:
    def __init__(self, name: str, age: int = 0, happiness: int = 50, hunger: int = 100):
        self.name = name
        self.age = age
        self.happiness = happiness
        self.hunger = hunger    
        self.alive = True
    
    def feed(self): #feeding is 25 pts, hunger max is 100.
        self.hunger += 25
        if self.hunger > 100:
            self.hunger = 100

    def play(self): #playing is 50pts, happiness max is 100.
        self.happiness += 50
        if self.happiness > 100:
            self.happiness = 100

    def gametick(self):
        self.age += 1
        self.hunger -= 5
        self.happiness -= 10
        self.update_status() 

    def update_status(self):
        if self.hunger < 0:
            self.hunger = 0
        if self.happiness < 0:
            self.happiness = 0
        if self.hunger == 0 and self.happiness == 0:
            self.alive = False
        else:
            self.alive = True    

    def __str__(self):
        status = "Alive" if self.alive else "Dead"
        return f"{self.name} - Age: {self.age}, Happiness: {self.happiness}, Hunger: {self.hunger} status: {status}"    
    
# if __name__ == "__main__":
#     # Maak een Gotchi aan
#     g = Gotchi("Gotchi")

#     # Print beginstatus
#     print("Beginstatus:")
#     print(g)
#     print("-" * 30)

#     # Voer een paar acties uit
#     print("Feed en Play acties:")
#     g.feed()
#     print("after feed:")
#     print(g)
#     g.play()
#     print("Na play:")
#     print(g)
#     print("-" * 30)

#     # Roep een aantal gameticks aan
#     print("Gameticks:")
#     for i in range(10):
#         g.gametick()
#         print(f"Tick {i+1}: {g}")
#         if not g.alive:
#             print("Je Gotchi has died!!")
#             break


# # while loop (time.sleep)
# # sleep method implementeren
# # 