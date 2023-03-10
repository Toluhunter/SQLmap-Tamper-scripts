__priority__ = 0


def tamper(payload, **kwargs):
    full_encode = ''
    for character in payload:
        full_encode += fr'&#{hex(ord(character))[-3:]};'

    return full_encode


if __name__ == "__main__":
    print(tamper(input("Enter payload: ")))
