def palindromo():
    something = input("Ingrese una frase, o nombre: ")

    
    if something == something[::-1]:
        print("Es un palindromo")
    elif something.replace(" ", "") == something.replace(" ", "")[::-1]:
        print("Es un palindromo")
    else:
        print("No es un palindromo")


# Entrypoint        
if __name__ == '__main__':
    palindromo()


