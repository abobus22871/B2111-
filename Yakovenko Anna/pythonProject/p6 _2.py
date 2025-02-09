ch1 = float(input("Write first number:"))
ch2 = float(input("Write second number:"))

try:
    result = ch1/ch2
    print(result)
except:
    print(f"vi namagalis : {ch1} na {ch2} i otrimatu pomilku")
    if ch2 == 0:
        print("na 0 dilutu ne mozna")
else:
    print("rosraxynku zavercheno")