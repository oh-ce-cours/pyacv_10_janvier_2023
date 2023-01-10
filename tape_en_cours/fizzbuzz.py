def regle_fizz_buzz(nombre):
    res = nombre
    if res % 3 == 0 and res % 5 == 0:
        res = "fizzbuzz"
    elif res % 3 == 0:
        res = "fizz"
    elif res % 5 == 0:
        res = "buzz"

    return res
