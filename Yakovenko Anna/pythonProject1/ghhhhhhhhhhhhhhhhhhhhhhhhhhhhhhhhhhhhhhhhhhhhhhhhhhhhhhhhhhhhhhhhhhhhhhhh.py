def checker(function, *args, **kwargs):
    def checker(*args, **kwargs):

        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"we have problemka - {exc}")
        else:
            print(f"NO PROBLEMS - {result}")

    return checker

def calculate(expression):
    return eval(expression)

calculate = checker(calculate)
calculate("2+2")