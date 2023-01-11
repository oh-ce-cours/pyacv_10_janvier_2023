from typing import Union


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


def regle_fizz_buzz_3(nombre):
    res = ""
    if nombre % 3 == 0:
        res += "fizz"
    if nombre % 5 == 0:
        res += "buzz"
    if not res:
        res = nombre
    return res


def regle_fizz_buzz(nombre: int) -> str:
    div_par_3 = nombre % 3 == 0
    div_par_5 = nombre % 5 == 0

    res = "fizz" * int(div_par_3) + "buzz" * int(div_par_5)
    res = res or str(nombre)
    return res


for nombre in range(1, 101):
    print(regle_fizz_buzz("tto"))

### équivalent à

[regle_fizz_buzz(nombre) for nombre in range(1, 101)]
