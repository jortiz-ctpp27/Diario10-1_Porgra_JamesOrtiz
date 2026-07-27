"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_promedio(lista):
    """Recibo una lista, la sumo y retorno el promedio"""
    promedio = sum(lista) / len(lista)
    return promedio

def calcular_logro_meta(lista_ventas, meta):
    """Cálcula el porcentaje del logro de la meta"""
    total_ventas = (sum(lista_ventas))
    return (total_ventas * 100) / meta

def calcular_clasificacion (porcentaje):
    if porcentaje >= 100:
        mensaje = "felicidades, meta alcanzada, sigue así!"
    elif porcentaje >= 80:
        mensaje = "llamada atención, debe trabajar por la meta..!"
    else:
        mensaje = "URGENTE, crisis de ventas. Atención prioritaria!"
    
    return mensaje

def imprimir_reporte(datos_reporte):
    """imprime el reporte final de ventas por sede."""
    print("\n REPORTE FINAL")
    print("-" * 60)
    #se recorre cada fila del reporte
    for fila in datos_reporte:
        print(f"sede: {fila["provincia"]}")
        print(f"provincia: {fila["provincia"]}")
        print(f"tipo: {fila["tipo"]}")
        print(f"total semanal: {fila["total"]:,.0f}")
        #se imprime el promedio diario con formato de moneda y sin decimales
        print(f"Promedio diario: {fila["total"]:,.0f}")
        #Se imprime el porcentaje con dos decimales
        print(f"Cumplimiento: {fila["porcentaje"]:.2f}")
        print(f"Estado: {fila["estado"]}")
        print("-" * 60)
    print("Cantidad de sedes:", len(datos_reporte))
        

#print("Tipo sedes:", type(sedes).__name__)
#print("Cantidad de empredimientos:", len(sedes))
#primer_emprendimiento = sedes[0]
#print("Tipo indice [0]:", type(primer_emprendimiento).__name__)
#print("empendimiento:", primer_emprendimiento["nombre"])
#print("Ventas emprendimiento", sum(primer_emprendimiento["ventas"]))
#promedio_diario = calcular_promedio(primer_emprendimiento["ventas"])
#porcentaje_logro = calcular_logro_meta(primer_emprendimiento["ventas"], primer_emprendimiento["meta"])
#print("Promedio diario de ventas:", promedio_diario)
#print(f"Porcentaje logro: {porcentaje_logro:.2f}")

reporte = []
for emprendimiento in sedes:
    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]
    nombre = emprendimiento["nombre"]
    promedio_diario = calcular_promedio(ventas)
    porcentaje_logro = calcular_logro_meta(ventas, meta)
    clasificacion = calcular_clasificacion(porcentaje_logro)
    
    reporte.append(
        {
            "nombre": nombre,
            "provincia": emprendimiento["provincia"],            
            "tipo": sum(emprendimiento["ventas"])
            "promedio": promedio_diario,
            "porcentaje": porcentaje_logro
            "estado": clasificacion
        }
    )
    imprimir_reporte(reporte)
    #print(f"\n---Emprendimiento {nombre}---\n")
    #print("Promedio diario de ventas:", promedio_diario)
    #print("Porcentaje logro:" , porcentaje_logro)
    #print("clasificación:", clasificacion , "\n")



