from mpmath import mp, factorial as fact, power


mp.prec = 2**17


def calc_step(k: int):
    assert k >= 0
    return (
        fact(6 * k)
        * (13591409 + 545140134 * k)
        / (fact(3 * k) * power(fact(k), 3) * power(640320, 3 * k + 1.5))
    )


def full(n: int):
    return 1 / (12 * sum(calc_step(k) for k in range(n)))


if __name__ == "__main__":
    calc = full(25)
    print(calc)
    print(len(str(calc)) - 1)
