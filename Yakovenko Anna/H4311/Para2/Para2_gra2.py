from random import randint

def coin():
    c = randint(0,1)
    if c ==  0:
        print("No")
    else:
        print("Yes")
    return c

how = int(input("How many coin?: "))
count = 0
for i in range(how):
    count += coin()

print(f'{count}-"Yes", {how-count}-"No"')
