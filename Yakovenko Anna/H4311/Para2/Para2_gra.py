from random import randint

def coin():
    c = randint(0,1)
    if c ==  0:
        print("No")
    else:
        print("Yes")


how = int(input("How many coin?: "))
for i in range(how):
    coin()
