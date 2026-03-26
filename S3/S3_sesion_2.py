#Día 2: Excepciones
## Java dev: En Java, el compilador te obliga a manejar los errores (Checked Exceptions) y 
# la filosofía suele ser "Look Before You Leap" (LBYL - Mira antes de saltar: usar muchos if 
# para validar antes de actuar).

## Python dev: En Python, la filosofía oficial se llama EAFP: "Easier to Ask for Forgiveness 
# than Permission" (Es más fácil pedir perdón que pedir permiso). Las checked exceptions no existen,
# por lo tanto todo sucede en tiempo de ejecución. 
def dividir(x: int,y: int):
    try:
        return x/y
    except ZeroDivisionError as ex:
        print(ex)
        return -1

def raiz_cuadrada(x: int):
    if x < 0:
        raise ValueError("Error - Raíz cuadrada de número negativo")
    return x ** 0.5
try:
    n1 = int(input("N1: "))
    n2 = int(input("N2: "))
    res = dividir(n1, n2)
except ValueError as ex:
    print(ex)
else:
    print(f"Resultado: {res}")

"""try:
    n = int(input("N: "))
    res = raiz_cuadrada(n)
except ValueError as ex:
    print(ex)

else:
    print(f"Resultado: {res}")"""

