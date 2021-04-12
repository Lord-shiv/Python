from prime import is_prime


def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"ERROR on is_prime({n}), expected {expected}")


# from test0 imort test_prime
# test_prime(5, True) --> no output
# test_prime(10, False) --> no output
# test_prime(25, False) --> Error
