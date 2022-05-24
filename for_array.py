from cgitb import text


def run():
    text_dummy = input("Ingresa una frase: ")


    for word in text_dummy:
        print(word)


if __name__ == "__main__":
    run()

