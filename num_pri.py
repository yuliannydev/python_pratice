def primo(value):
    
    for num in range(1, value + 1):
        pass


def run():
    number = int(input("Ingrese un número: "))
    

    if primo(number):
        print("Es número primo.")
    else:
        print("No es número primo.")


if __name__ == '__main__':
    run()