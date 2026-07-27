#SISTEMADE DE CONTROL DE AFORO DEL CENAC
#Autor: James Ortiz
#Fecha: 2026-07-21

#
CAPACIDAD_MAXIMA = 700  
UMBRAL_PREVENTIDO = 560

grupos_aceptados = []
grupos_rechazados = []
ocupacion_actual = 0

print("CONTROL DE INGRESO - ANFITEATRO DEL CENAC")
print("Capacidad máxima: 700 personas")
print("Escriba FIN para cerrar el programa.\n")

entrada = input("Cantidad de personas en el grupo: \n").lower().strip()

while entrada != "fin":
    try:
        cantidad_grupo = int(entrada)
    except ValueError:
        print("Error: Ingrese un número válido o 'FIN' para salir.")
    else:
        if cantidad_grupo < 0:
            print("ERROR: cantidad de personas no válida")
        elif cantidad_grupo + ocupacion_actual <= CAPACIDAD_MAXIMA:
            grupos_aceptados.append(cantidad_grupo)
            ocupacion_actual += cantidad_grupo
            espacios_disponibles = CAPACIDAD_MAXIMA - ocupacion_actual
            print(f"Grupo aceptado. ingresan {cantidad_grupo} personas")
            print(f"Ocupación actual: {ocupacion_actual} ")
            print(f"Espacios disponibles: {espacios_disponibles}")
        else:
            grupos_rechazados.append(cantidad_grupo)
            espacios_disponibles = CAPACIDAD_MAXIMA - ocupacion_actual
            print(f"Grupo rechazado. No hay espacio para {cantidad_grupo} personas")
            print(f"Ocupación actual: {ocupacion_actual} ")
            print(f"Espacios disponibles: {espacios_disponibles}")
    entrada = input("Cantidad de personas en el grupo: \n").lower().strip()