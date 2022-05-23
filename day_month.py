def new_func():
    fecha = input("¿Qué fecha es hoy? ")
    fecha = int(fecha)
    mes = 31
    result = mes - fecha
    result = str(result)
    print("Al mes le quedan " + result + " días")


new_func()
