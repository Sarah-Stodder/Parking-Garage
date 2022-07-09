
class ParkingGarage:
    MAX_SPACES = 10

    def __init__(self):
        self.parking_spaces = {}
        self.name = ""
        self.tickets = 10
        self.spots = 0
    def random(self):
         if self.tickets == 0:
           print("Theres no space for you here!")
         else:
                self.spots+=1
                self.tickets -= 1

         print(f'There are {self.tickets} parking spaces left')
         print(f"{self.spots} Spots occupied")

    def adding(self):
        self.name = input("What is your first name? ")
        # self.parking_spaces(self.name)
       
        self.parking_spaces[self.name] = 15.00
        print(self.parking_spaces)

    def deleting(self):    
        self.name = input("What  is your name? ")
        print(f"{self.name} Swipe your card!")
        for item in self.parking_spaces:
            if item == self.name:
                self.parking_spaces[self.name] = "paid"
                print(self.parking_spaces)
                del self.parking_spaces[self.name]
                print("You're all settled up, come again!")
                self.spots -= 1
                self.tickets +=1 
                return
            else:
                print("Dude where's your car? it's not here!")
              






class Kiosk ():
    parking_garage = ParkingGarage()
    @classmethod
    def main(self):
          while True:
            response = input("Would you like to Park, Settle up, or Leave garage? ")
            if response[0].lower() == "l":
                print ("Ok. Take your car and go.")
                break
            elif response[0].lower() == "p":
                self.parking_garage.adding()
                self.parking_garage.random()
            elif response[0].lower() == "s":
                self.parking_garage.deleting()
            else:
                print("That command is not valid. Please try again")


if __name__ == "__main__":
    Kiosk.main()
        