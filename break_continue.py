# def run():
#     for indice in range(100):
#         if indice % 2 != 0:
#             continue
#         print(indice)


# if __name__ == "__main__":
#     run()

def run():
    text_dummy = input("Ingrese un texto dummy: ")
    for letter in text_dummy:
        if letter == "a":
            break
        print(letter)

if __name__ == "__main__":
    run()