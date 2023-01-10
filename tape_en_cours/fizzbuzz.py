def regle_fizz_buzz_1(nombre):
    res = nombre
    if nombre % 3 == 0 and nombre % 5 == 0:
        res = "fizzbuzz"
    elif nombre % 3 == 0:
        res = "fizz"
    elif nombre % 5 == 0:
        res = "buzz"
    return res


def regle_fizz_buzz_2(nombre):
    if nombre % 3 == 0 and nombre % 5 == 0:
        return "fizzbuzz"
    if nombre % 3 == 0:
        return "fizz"
    if nombre % 5 == 0:
        return "buzz"
    return nombre


def regle_fizz_buzz(nombre):
    res = ""
    if nombre % 3 == 0:
        res += "fizz"
    if nombre % 5 == 0:
        res += "buzz"
    if not res:
        res = nombre
    return res


for nombre in range(1, 101):
    print(regle_fizz_buzz(nombre))

### équivalent à

[regle_fizz_buzz(nombre) for nombre in range(1, 101)]
