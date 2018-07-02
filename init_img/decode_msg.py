def caesar_decode_ascii(dif_to: int, cipher_text: str) -> str:
    str = ""
    for c in cipher_text:
        str += chr(ord(c) + dif_to)
    return str


def main():
    f = open("msg.txt")
    msg = f.read()
    index_start = msg.find("\"")
    cipher_text = msg[index_start:].replace("\"", "")
    dif = ord('h') - ord(cipher_text[0])
    print(caesar_decode_ascii(dif, cipher_text))


if __name__ == "__main__":
    main()
