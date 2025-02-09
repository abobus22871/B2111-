def checker(var1):
    if type(var1) != str:
        raise TypeError(f'mi ne mozemo pracyvatu z takum tupom danux - {type(var1)}, Treba tup - str')
    else:
        return var1


my_var = 10
my_var2 = "ABOBA"
checker(my_var)
checker(my_var2)
