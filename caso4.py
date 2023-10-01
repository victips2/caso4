from casosGeneradosP45 import *
from functools import reduce

def recaudoModelosDefectuosos(caso: dict) -> dict:
# """Desarrollar aquí el requerimiento. Se recomienda el uso de las funciones
# map, filter, reduce y opcionalmente zip, para realizarlo con mayor facilidad."""
    listadoCajerosNoOperando = list(filter(lambda cajero: caso[cajero]['estado'] != 'Operando', caso))

    numeroConsignaciones = reduce(lambda x, y: x + y, list(map(lambda cajero: len(list(filter(lambda transaccion: transaccion['tipoMovimiento'] == 'consignacion', caso[cajero]['transacciones']))), listadoCajerosNoOperando))) 

    totalRecaudado = reduce(lambda x,y : x + y, list(map(lambda cajero: reduce(lambda x,y : x + y['monto'], list(filter(lambda transaccion: transaccion['tipoMovimiento'] == 'consignacion', caso[cajero]['transacciones'])), 0), listadoCajerosNoOperando)))

    listadoModelosFallando = sorted(dict.fromkeys(list(map(lambda cajero: caso[cajero]['modeloCajero'], listadoCajerosNoOperando))))

    respuesta = {'numeroConsignaciones': numeroConsignaciones, 'totalRecaudado': totalRecaudado, 'listadoModelosFallando': listadoModelosFallando}
    
    return respuesta

print(recaudoModelosDefectuosos(caso2))