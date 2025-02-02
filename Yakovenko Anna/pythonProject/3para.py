import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.madness = 0
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(list_of_job)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
               self.satiety  = 100
            self.satiety += 5
            self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salry
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                  manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I buy fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("i buy food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicacies")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15



    def chill(self):
        self.gladness += 10
        self.home.mess += 5


    def clean_house(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self , day):
        print(f"Today is {day} of {self.name} life")
        print(f"Money - {self.money}\nGladness - {self.gladness}\nSatiety - {self.satiety}")
        print(f"Home\nFood - {self.home.food}\nMess - {self.home.mess}")
        print(f"Car\nFuel - {self.car.fuel}\nStrengh - {self.car.strengh}")
    def is_alive(self):
        if self.gladness < 0:
            print("Depresion")
            return False
        if self.satiety < 0:
            print("Dead")
        if self.money < -500:
            print("Bankrot")
            return False



    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
             print("Setled the house")
             self.get_home()
        if self.car is None:
            self.get_car()
            print(f"i buy car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"i get job - {self.job.job}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
              self.eat()
        elif self.gladness <20:
            self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strengh < 15:
            self.to_repair()
            if dice == 1:
                print("lets chill guy")
                self.chill()
            elif dice == 2:
                print("go to work")
                self.work()
            elif dice == 3:
                print("Cleaning time")
                self.clean_house()
            elif dice == 4:
                print("Time to treats")
                self.shopping("delicacies")





class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strengh = brand_list[self.brand]["strengh"]
        self.consumption = brand_list[self.brand]["consuption"]

    def drive(self):
        if self.strengh > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strengh -= 1
            return True
        else:
            print("The car cannot move!")
            return False

brands_of_car = {
    "BMW":{"fuel": 100,"strengh": 100, "consuption": 6},
    "Audi":{"fuel": 50,"strengh": 40, "consuption": 10},
    "Volvo":{"fuel": 70,"strengh": 150, "consuption": 8},
    "Ferrari":{"fuel": 80,"strengh": 120, "consuption": 14},
}

class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:
   def __init__(self, job_list):
       self.job = random.choice(list(job_list))
       self.salary = job_list[self.job]["salary"]
       self.gladnes_less = job_list[self.job]["gladness_less"]

list_of_job = {
    "Java developer": {"salary": 50, "gladness_less":10},
    "Python developer": {"salary": 40, "gladness_less":3},
    "C++ developer": {"salary": 45, "gladness_less":25},
    "Rust delevoper": {"salary": 45, "gladness_less":3},
}

my_human = Human(name="ABOBA")
for day in range(1,8):
    if my_human.live(day) == False:
        break