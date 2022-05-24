def conversor():
    moneda = int(input("Ingrese el monto de dinero que desea convertir: "))
    valor_dolar = int(input("Ingrese el valor del dolar en su moneda: "))
    valor_total = moneda / valor_dolar
    valor_total = round(valor_total, 2)
    valor_total = str(valor_total)
    print("Ud tiene $USD" + valor_total)


conversor()