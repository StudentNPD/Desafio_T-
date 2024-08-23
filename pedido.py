from te import Te
from validate import validate



sabor = validate([1, 2,3],int(
    input(
        "¿Qué sabor de té desea? (Ingrese número de la opción)"
        "\n1. Té negro \n2. Té verde \n3. Agua de hierbas\n"
    )
))

formato = validate([500, 300],int(
    input(
        "¿Qué formato desea?. Tenemos disponible"
        " 300 y 500 gramos. Ingrese la cantidad de gramos deseada\n"
    )
))

#tiempo, recomendacion = Te.retorna_precio(sabor )
#precio = Te.retorna_tiempo_y_recomendacion(formato)
precio = Te.retorna_precio(formato)
tiempo, recomendacion = Te.retorna_tiempo_y_recomendacion(sabor)

if sabor == 1:
    sabor_texto = "Té negro"
elif sabor == 2:
    sabor_texto = "Té verde" # Te rojo
elif sabor == 3:
    sabor_texto = "Agua de hierbas"


print(
    "Se ingresó su pedido de {}, en formato de {} gramos,"
    "el cual tiene un valor de ${}. Este té tiene un tiempo "
    "de preparación de {} minutos, y se recomienda su uso {}.".format(
        sabor_texto, formato, precio, tiempo, recomendacion
    )
)

# Confundir sabores 
# El tiempo es el correcto?
# Retorno de tiempo y recomendaciónes
# hay un sabor que no deberia existir 
# valor 