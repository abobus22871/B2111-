ch1 = float(input("Write first number:"))
ch2 = float(input("Write second number:"))
ch3 = float(input("Write third number:"))

def check(ch1, ch2, ch3,):
     if ch1 % 5 == 0:
         if ch2 % 5 == 0:
            if ch3 % 5 == 0:
                sp = [ch1, ch2, ch3]
                sp.sort()
                print(sp)
     else:
         raise TypeError("nepravilne chislo vsi chisla mayt dilutusa na 5")
     else:
      raise TypeError("nepravilne chislo vsi chisla mayt dilutusa na 5")

else:
raise TypeError("nepravilne chislo vsi chisla mayt dilutusa na 5")



try:
    check(ch1, ch2, ch3)
except TypeError:
    print("vedeno necorektni chisla")






