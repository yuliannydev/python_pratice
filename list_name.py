def say_welcome(name):
    print("Bienvenida: ")
    print(name + "🥇")
    print("Te estabamos esperando.")

add_name = input("Ingresa tu nombre: ")
    
if add_name == "nathalie":
    say_welcome(add_name)
elif add_name == "yulianny":
    say_welcome(add_name)
else:
    print("Ud no se encuentra en la lista de invitados")
