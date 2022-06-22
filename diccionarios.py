def run():
    # diccionario = {
    #     'llave': 1,
    #     'llave2': 2,
    #     'llave3': 3,
    #     'llave4': 4,
    # }
    # print(diccionario)

    # for var_llave in diccionario.keys():
    #     print(var_llave)

    # for var_value in diccionario.values():
    #     print(var_value)


    diccionario = {
        'llave': 'valor 1',
        'llave2': 'valor 2',
        'llave3': 'valor 3',
        'llave4': 'valor 4',
    }

    for var_llave, var_value in diccionario.items():
        print('Para la ' + var_llave + ' su contenido es: ' + var_value)

if __name__ == '__main__':
    run()