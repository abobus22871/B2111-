from random import randint

def coin():
    c = randint(0,1)
    if c ==  0:
        print("No")
    elif: c > 50:
        print("Yes")
    else:
        print("Wow!")


how = int(input("How many coin?: "))
for i in range(how):
    coin()