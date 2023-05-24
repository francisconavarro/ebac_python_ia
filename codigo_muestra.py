"""
Script de ejercicio que muestra como definir variables, funciones y el uso de librerias
Python version: Python 3.8

"""
# importacion de libreria
import math


def print_title(_str_message, _bln_space=True):
    """
    Funcion que imprime un titulo en color predeterminado

    Parameters
    ----------
    _str_message:
                       Mensaje a imprimr

    btl_space:
                       bandera que indica si hay que agregar espacio al inicio
    """
    if _bln_space:
        print( '\n')
    print(('\x1b[0;37;44m' + '****************************************' + '\x1b[0m'))
    print(('\x1b[0;37;44m' + '* ' + _str_message.center( 36 ) + ' *'+ '\x1b[0m'))
    print(('\x1b[0;37;44m' + '****************************************' + '\x1b[0m'))


def print_message(_str_message):
    """
    Funcion que imprime un mensaje en color predeterminado

    Parameters
    ----------
    _str_message:
                       Mensaje a imprimr

    """
    print(('\x1b[0;37;45m' + str(_str_message) + '\x1b[0m'))


def print_error(_str_message):
    """
    Funcion que imprime un error en rojo

    Parameters
    ----------
    _str_message:
                       Mensaje a imprimr

    """
    print(('\x1b[1;33;41m' + str(_str_message) + '\x1b[0m'))


def print_values(_str_message):
    """
    Funcion que imprime valores en azul

    Parameters
    ----------
    _str_message:
                       Mensaje a imprimr

    """
    print(('\x1b[1;36;46m' + str(_str_message) + '\x1b[0m'))


def get_string(_str_message):
    """
    Funcion que lee un string de la consola

    Parameters
    ----------
    _str_message:
                       Mensaje a imprimr
    Returns
    -------
    string proporcionado por el usuario en el input
    """
    str_value = None
    while str_value is None:
        print_message(_str_message)
        str_value = input()
        if len(str_value) == 0:
            str_value = None
            print_error( "valor invalido!! intenta de nuevo...")

    return str_value


def get_int(_str_message):
    """
    Funcion que lee un entero de la consola

    Parameters
    ----------
    _str_message:
                       Mensaje a imprimr
    Returns
    -------
    int proporcionado por el usuario en el input
    """
    num_value = None

    while num_value is None:
        print_message(_str_message)
        try:
            num_value = int(input())
        except ValueError:
            print_error( "valor invalido!! intenta de nuevo...")

    return num_value


def get_float(_str_message):
    """
    Funcion que lee un float de la consola

    Parameters
    ----------
    _str_message:
                       Mensaje a imprimr
    Returns
    -------
    float proporcionado por el usuario en el input
    """
    flo_value = None

    while flo_value is None:
        print_message(_str_message)
        try:
            flo_value = float(input())
        except ValueError:
            print_error( "valor invalido!! intenta de nuevo...")

    return flo_value


def calcular_area_rectangulo(_flo_base, _flo_altura):
    """
    Funcion que calcula el area de un rectangulo

    Parameters
    ----------
    _flo_base:
                       base del rectangulo
    _flo_altura:
                       altura del rectangulo
    Returns
    -------
    el area del rectangulo
    """
    return _flo_base * _flo_altura


# Recepcion de variables
print_title('Recepcion de variables', False)
str_nombre     = get_string("Proporciona el nombre: ")
num_edad       = get_int("Proporciona la edad: ")
flo_altura     = get_float("Proporciona la altura: ")
bln_estudiante = (input(('\x1b[0;37;45m' +"Es estudiante:"+ '\x1b[0m')).lower() in ('true', 'yes'))

# Impresion de variables
print_title('Impresion de variables')
print_values("Mi nombre es: " + str_nombre)
print_values("Tengo " + str(num_edad) + "años")
print_values("Mi altura es " + str(flo_altura) + " metros")
print_values("¿Soy estudiante " + str(bln_estudiante))

# Estructuras de control: condicionales
print_title('Manejo de flujos de control IF-Else')
if num_edad >= 18:  # Si la edad es mayor o igual a 18
    print_values("Soy mayor de edad")
else:
    print_values("Soy menor de edad")

# Ciclo while
print_title('Manejo de Ciclo While')
NUM_CONTADOR = 0
num_limite = get_int("Cuantas iteraciones quieres hacer en el ciclo while?")
while NUM_CONTADOR < num_limite:
    NUM_CONTADOR += 1
    print_values("El contador es: " + str(NUM_CONTADOR))

# Ciclo for
print_title('Recorrer Diccionario con ciclo For')
dict_frutas = get_string("Proporciona Frutas separado por coma ").split(",")
for str_fruta in dict_frutas:
    print_values("Me gusta comer: " + str_fruta)

# Calculo de Area de dos Rectangulos
NUM_CONTADOR = 1
print_title('Manejo de Funciones')
while NUM_CONTADOR < 3:
    base_rectangulo = get_float(("Proporciona la base del rectangulo " + str( NUM_CONTADOR)))
    altura_rectangulo = get_float(("Proporciona la altura del rectangulo " + str(NUM_CONTADOR)))
    area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
    print_values("El area del rectangulo "+ str(NUM_CONTADOR) + " es: " + str(area_rectangulo))
    NUM_CONTADOR += 1

# Calculo de raiz cuadrada
print_title('Usar modulos importados')
num_cuadrado = get_int("Proporciona el numero al que le quieres sacar raiz cuadrada:")
raiz_cuadrada = math.sqrt(num_cuadrado)
print_values("La raíz cuadrada de" + str(num_cuadrado)  + " es:" + str(raiz_cuadrada))
