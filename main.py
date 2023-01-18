rentedskies = 0
rentedboards  = 0
class ski_rentals:
    def __init__(self, skies, snowboards, dayprice, hourprice):
        self.skies = skies
        self.snowboards = snowboards
        self.dayprice = dayprice
        self.hourprice = hourprice
    def display(self):
        print("Number of skies :")
        print(self.skies)
        print("Number of Snowboards")
        print(self.snowboards)
    def budget(self, budgetnum):
        if budgetnum >= self.dayprice:
            print("You can afford a day rental for " + str(self.dayprice) +"$ , or")
        if budgetnum >= self.hourprice:
            print("You can afford hourly retals for " + str(self.hourprice) +"$ per hour")
    def rentboard(self, num):
        self.snowboards = self.snowboards - num
        if num >= self.snowboards:
            print("sorry we dont have enough snowboards")
        rentedboards + num
        print("you have rented" + str(num) + "boards")
        var = input("day or hourly")
        if var == "day":
            print("-20$")
        elif var == "hourly":
            print("-10$")
    def rentskies(self, num):
        self.skies = self.skies - num
        if self.skies >= 0:
            print("sorry we dont have enough skies")
        rentedskies = rentedskies + num
        print("you have rented" + num + "skies")
        var = input("day or hourly")
        if var == "day":
            print("-20$")
        elif var == "hourly":
            print("-10$")
    def returnrentals(self):
        self.skies = self.skies + rentedskies
        rentedskies = 0
        self.snowboards = self.snowboards + rentedboards
        rentedboards = 0

sunridge =  ski_rentals(3, 4, 20, 10)
sunridge.display()
sunridge.budget(20)
sunridge.rentboard(4)
