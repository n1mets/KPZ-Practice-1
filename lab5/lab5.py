import lab3


def test_prime_num_generator():
    generator = lab3.prime_num_generator()
    counter = 0

    for i in range(0, 101):
        value = next(generator)
        if (i == 2 or i % 2 != 0) and (i == 3 or i % 3 != 0) and (i == 5 or i % 5 != 0) and (i == 7 or i % 7 != 0) and counter < 12:
            assert value == i
            counter += 1
        if i == 101:
            assert value == 101


def test_palindrom():
    assert lab3.palindrom() == []

    try:
        lab3.palindrom(24)
    except TypeError:
        assert True

    assert lab3.palindrom("radar banana") == ["radar"]

    assert lab3.palindrom("hannah pup nan eye 6543456 deed") == [
        "hannah", "pup", "nan", "eye", "deed"]
    assert lab3.palindrom("lollipop8*(/) 6543456^&%$?") == []


def test_validate_ip():
    assert lab3.validate_ip("123.667") == False
    assert lab3.validate_ip() == False
    assert lab3.validate_ip("0.0.0.0") == True
    assert lab3.validate_ip("266.244.85.100") == False
    assert lab3.validate_ip("253.223.50.66") == True

    try:
        lab3.palindrom(577)
    except TypeError:
        assert True


def test_get_os():
    assert lab3.get_os() == "Windows"
