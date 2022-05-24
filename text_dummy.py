## Generator text dummy
## Change the vowel in the text for whatever wowel you want


def run():
    text_dummy = input("Ingrese un texto dummy: ")
    letter_dummy = input("Ingrese la vocal para el texto dummy: ")


    for letter in text_dummy:
        if letter == "a":
            print(letter.replace("a", letter_dummy))
            continue
        elif letter == "e":
            print(letter.replace("e", letter_dummy))
            continue
        elif letter == "i":
            print(letter.replace("i", letter_dummy))
            continue
        elif letter == "o":
            print(letter.replace("o", letter_dummy))
            continue
        elif letter == "u":
            print(letter.replace("u", letter_dummy))
            continue
        print(letter)


if __name__ == "__main__":
    run()