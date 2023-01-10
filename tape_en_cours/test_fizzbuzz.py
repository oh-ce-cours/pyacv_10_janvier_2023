from fizzbuzz import regle_fizz_buzz


def test_regle():
    assert regle_fizz_buzz(3) == "fizz"
    assert regle_fizz_buzz(5) == "buzz"
    assert regle_fizz_buzz(15) == "fizzbuzz"
    assert regle_fizz_buzz(4) == 4
