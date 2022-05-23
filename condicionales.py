day = int(input("Ingresa la fecha de hoy: "))
if day > 31:
    print("Debe ingresar una fecha correcta. ")
    day = int(input("Ingresa la fecha de hoy: "))
month = int(input("¿Cuántos días tiene este mes? "))
if month > 30:
    result = month - day
else:
    result = month - day
result = str(result)
print("Al mes le quedan " + result + " dias")
