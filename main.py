## Harrison Tenganan Colorado
## Archivo de operaciones

def sumar(x,y):
    return (x + y)

def restar(x,y):
    return (x - y)

def multiplicar(x,y):
    return (x * y)

def dividir(x,y):
    if y == 0:
        raise ValueError("Indeterminacion, division entre 0")
    return (x / y)