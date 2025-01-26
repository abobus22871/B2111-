import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        if self.gladness <= 0:
            print("depresion :(")
            self.alive = False
        if self.progress > 5:
            print("Passed externally")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")

    def live(self, day):
        text = f"Day {day} of {self.name} life"
        print(f"{text:=^30}")
        live_cube = random.randint( 1,  3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
             self.to_sleep()
        elif live_cube == 3:
             self.to_chill()
        self.end_of_day()
        self.is_alive()


student = Student("aboba")

for day in range(365):
    if student.alive:
        student.live(day)
    else:
        break