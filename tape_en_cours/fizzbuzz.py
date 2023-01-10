def regle_fizz_buzz_1(nombre):
    res = nombre
    if nombre % 3 == 0 and nombre % 5 == 0:
        res = "fizzbuzz"
    elif nombre % 3 == 0:
        res = "fizz"
    elif nombre % 5 == 0:
        res = "buzz"
    return res


def regle_fizz_buzz(nombre):
    if nombre % 3 == 0 and nombre % 5 == 0:
        return "fizzbuzz"
    if nombre % 3 == 0:
        return "fizz"
    if nombre % 5 == 0:
        return "buzz"

    return nombre
