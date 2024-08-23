def validate(formato, sabor):

    while sabor not in formato:
        print(f'Opción no válida, ingrese una de las opciones válidas: {formato}')
        sabor = int(input("Ingresa una opción: "))
    return sabor