import json
import pygame
from os import system



def cargar_json(path: str):
    '''
    Esta funcion recibe un archivo.json y lo carga de forma que se pueda usar en una variable retornada.
    Parametros: path del tipo str
    Retorna: Retorna una variable con la carga del archivo.
    '''
    with open(path, 'r') as archivo:
        carga_de_datos = json.load(archivo)

    archivo.close

    #print("¡DATOS DEL ARCHIVO CARGADOS CON EXITO!")

    return carga_de_datos["jugadores"]

def guardar_jugador(nombre_jugador: str, score: int, diccionario_jugadores: list):
    '''
    Esta funcion tiene como objetivo guardar el score y nombre del jugador que acaba de realizar la partida, para luego compararlo con los rankings existentes en otra funcion.
    Parametros: nombre_jugador del tipo str, score del tipo int
    Retorna: No tiene retorno.
    '''
    
    diccionario_nuevo = {}

    diccionario_nuevo.update({"nombre_jugador": nombre_jugador})
    diccionario_nuevo.update({"Score": score})

    diccionario_jugadores.append(diccionario_nuevo)

    return diccionario_jugadores

def verificar_nombres_juego(nombre: str, caracteres: int):
    '''
    Esta funcion verifica la longitud de un nombre, confirma si este cumple los requisitos ingresados por parametro
    Parametros: nombre del tipo str, caracteres del tipo int
    Retorna: Booleano
    '''

    verificacion = False

    if len(nombre) < caracteres:
        verificacion = True

    return verificacion

def ordenar_diccionarios(lista: list, clave: str, criterio: str = ">"):

    '''
    Esta funcion recorre una lista dada con su tamaño correspondido y con una clave en particular va comparando si los valores de esas claves son mayores o menores (si son strings las ordena de forma alfabetica, si son ints las ordena de forma ascendente)
    Parametros: Lista del tipo list, clave del tipo str
    '''
    for i in range(len(lista)):
        for valores in range(len(lista)-1):
            if criterio == ">" and (lista[valores][clave] > lista[valores+1][clave]) or criterio == "<" and (lista[valores][clave] < lista[valores+1][clave]):
                aux = lista[valores]
                lista[valores] = lista[valores+1]
                lista[valores+1] = aux

def guardar_json(path: str, lista: str):
    '''
    Abre un nuevo JSON para guardar determinados datos.
    Parametros: path str, lista del tipo str
    '''

    with open(path, 'w') as archivo:

        json.dump({"jugadores":lista}, archivo, indent = 4)

def controlar_musica(control: bool, musica1, musica2, musica3, musica4, musica5, musica6):
    '''
    Esta funcion controla los volumenes de la musica que se le agrega por parametros.
    Parametros: control del tipo bool, musica1, musica2, musica3, musica4, musica5, musica6
    Retorno: Retorna un booleano.
    '''

    if control == False:
        musica1.set_volume(0)
        musica2.set_volume(0)
        musica3.set_volume(0)
        musica4.set_volume(0)
        musica5.set_volume(0)
        musica6.set_volume(0)
        control = True
                    
    else:
        musica1.set_volume(1)
        musica2.set_volume(0.05)
        musica3.set_volume(0.05)
        musica4.set_volume(2)
        musica5.set_volume(2)
        musica6.set_volume(0.05)
        control = False

    return control




