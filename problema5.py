# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Problema 3 - Auditoría de Inventario

# MATRIZ DE INVENTARIO
# [Código, Nombre, Stock Actual, Stock Mínimo]

inventario = [
    ["A101", "Mouse", 5, 10],
    ["A102", "Teclado", 12, 10],
    ["A103", "Monitor", 3, 8],
    ["A104", "Memoria USB", 20, 15],
    ["A105", "Impresora", 1, 5]
]
# FUNCIÓN PARA CALCULAR LA CANTIDAD A PEDIR

def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0

    return cantidad_pedir

# FUNCIÓN PARA MOSTRAR INVENTARIO

def mostrar_inventario():

    print("\n==========================================")
    print("         INVENTARIO DISPONIBLE")
    print("==========================================")

    for articulo in inventario:

        print("Código:", articulo[0],
              "| Artículo:", articulo[1])

    print("==========================================")

# FUNCIÓN PARA CONSULTAR PRODUCTO

def consultar_producto(codigo_busqueda):

    encontrado = False

    for articulo in inventario:

        codigo = articulo[0]

        if codigo == codigo_busqueda:

            nombre = articulo[1]
            stock_actual = articulo[2]
            stock_minimo = articulo[3]

            cantidad_pedir = calcular_pedido(
                stock_actual,
                stock_minimo
            )

            print("\n==========================================")
            print("         RESULTADO DE CONSULTA")
            print("==========================================")

            print("Código del producto:", codigo)
            print("Nombre del producto:", nombre)
            print("Stock actual:", stock_actual)
            print("Stock mínimo requerido:", stock_minimo)
            print("Cantidad a solicitar:", cantidad_pedir)

            if cantidad_pedir > 0:
                print("Estado: REABASTECER")
            else:
                print("Estado: STOCK SUFICIENTE")

            print("==========================================")

            encontrado = True

    if encontrado == False:
        print("\nEl código ingresado no existe.")

# PROGRAMA PRINCIPAL

print("==========================================")
print("    SISTEMA DE AUDITORÍA DE INVENTARIO")
print("==========================================")

continuar = "SI"

while continuar == "SI":

    mostrar_inventario()

    codigo = input(
        "\nIngrese el código del producto: "
    )

    consultar_producto(codigo)

    continuar = input(
        "\n¿Desea consultar otro producto? (SI/NO): "
    )

    continuar = continuar.upper()

print("\nGracias por utilizar el sistema.")

