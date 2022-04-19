from asyncio.windows_events import NULL
import sys


def prime_num_generator():
    num = 0
    while True:
        yield num
        num += 1


#   Palindrom

def palindrom(line: str = "") -> list:

    if not isinstance(line, str):
        raise TypeError

    wordArr = []
    word = ""

    line = line.lower()

    for index, i in enumerate(line):
        if not i.isalpha():
            if len(word) != 0:
                wordArr.append(word)
                word = ""
        else:
            word += i
            if index == len(line)-1:
                wordArr.append(word)
                word = ""

    result = []
    for el in wordArr:
        check = True
        for i in range(len(el)//2):
            if el[i] != el[len(el)-1-i]:
                check = False
                break
        if check:
            result.append(el)

    return result


#   Validate


def validate_ip(ip_address: str = ""):
    if not isinstance(ip_address, str):
        raise TypeError

    if len(ip_address) == 0:
        return False

    elements = ip_address.split(".")
    if len(elements) != 4 or not elements[0].isdigit() or int(elements[0]) > 253:
        return False

    for el in elements:
        if not el.isdigit() or (int(el) < 0 or int(el) > 255):
            return False

    return True


#   OS

def get_os():
    platformName = sys.platform

    if platformName == "win32":
        return "Windows"
    elif platformName == "darwin":
        return "Mac"
    elif platformName == "linux":
        return "Linux"
    else:
        return "Unknown"
