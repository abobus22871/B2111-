def all_math_operation(a, b):
    dod = a + b
    vid = a - b
    mno = a * b
    if b == 0:
        dil = 'error'
    else:
        dil = a / b
    return dod, vid, mno, dil


res1, res2,res3, res4 = all_math_operation(20, 3)
print(res3, res4)

res11, res12, res13, res14 = all_math_operation(res1, res2)
print(res11, res12, res13, res14)