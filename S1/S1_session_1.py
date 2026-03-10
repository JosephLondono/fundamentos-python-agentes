#Día 1
##Entrada y salida de datos
###Entrada: input()
###Salida: print()

#Concatenación de funciones
nombre = input("¿Cuál es tu nombre?: ").lower().capitalize()
##Funciones para str
# upper()/lower()/capitalize() - ¿Qué otras funciones de str existen?
print("Hola %s, mucho gusto~" %(nombre))

#-----------------------------------------------------------#

#Tipos de datos primitivos - ¿Qué otros tipos de datos primitivos existen?
##%s: str - String - Texto
##%d: int - Integer - Numérico entero
##%f: float - Float - Numérico decimal
##%x bool - Boolean - Valor de verdad: Verdadero (true) o Falso (false)

#---------------------------------------------------------#

#Formas de hacer output (mostrar por pantalla)
##Por comas:
# - print("Hola ", nombre, "mucho gusto~" )
##Por placeholders
# %s: str
# %d: int
# %f: float
# ¿Cuál es el placeholder para el tipo de dato bool?
# - print("Hola %s, tu edad actual es %d" %(nombre, edad))
##Por .format()
# - print("Hola, {fname}. Mucho gusto~").format(fname=nombre)
# - print("Hola, {0}. Mucho gusto~").format(nombre)
# - print("Hola, {}. Mucho gusto~").format(nombre)
##Por concatenación (+)
# - #print("Hola  "+nombre+", tu edad actual es "+str(edad))

#-----------------------------------------------------------#

anio_nac= input("Ingresa tu año de nacimiento: ")
anio_act=2026
edad = anio_act-int(anio_nac)
nivel = input("Nivel de usuario: ")

sueldo = float(input("Ingresa tu sueldo: "))

print("Tu edad actual es: ", edad )
print("Hola %s, tu edad actual es %d" %(nombre, edad))

print("Hola  "+nombre+", tu edad actual es "+str(edad))
print("Sueldo actual: %.2f"%(sueldo))

#-------------------------------------------------------------#

##Lógica booleana - if/else - ¿Cómo sería el uso de if/elif/else?
#Operadores I: and, or, not
#Operadores II: >,<, >=,<=,==

#----------------------------------------------------------------#
if edad>=18 or nivel == "2" :
    print(f"Acceso concedido. Bienvenido a la terminal, {nombre}")
else:
    print("Acceso denegado")

##Ejemplo para estudios autónomos
print("--- Sistema de Seguridad Nivel 1 ---")

# 1. Recolección de datos (I/O)
nombre = input("Identifícate. ¿Cuál es tu nombre?: ")

# Demostrar la conversión explícita
edad_str = input("Ingresa tu edad: ")
edad = int(edad_str) 

tiene_credencial = input("¿Tienes credencial VIP? (si/no): ").lower() == "si"

# 2. Lógica Booleana y Control de Flujo (if/elif/else)
print("\nAnalizando credenciales...")

if edad >= 18 and tiene_credencial:
    # Uso de f-strings para formateo moderno
    print(f"Acceso Concedido. Bienvenido a la terminal, {nombre}.")
elif edad >= 18 and not tiene_credencial:
    print(f"Acceso Denegado. {nombre}, eres mayor de edad pero requieres pase VIP.")
else:
    # Se calcula cuánto falta para los 18
    print(f"Alerta de intruso. Te faltan {18 - edad} años para ingresar.")

##Mini-taller I: Ejercicio para práctica autónoma
### La IA generó un sistema de cálculo de bonos, pero está crasheando y 
# tomando decisiones ilógicas. ¿Puedes encontrar los 3 errores, 
# arreglarlos y mejorar los prints usando f-strings?
sueldo = input("Ingresa tu sueldo base: ")
anios_empresa = input("¿Cuántos años llevas en la empresa?: ")

bono = sueldo * 0.10 

if anios_empresa > 5:
    print("¡Felicidades! Tienes un bono extra por antigüedad.")
    total = sueldo + bono + 500
else:
    print("No hay bono de antigüedad.")
    total = sueldo + bono

print("Tu total a recibir es:")
print(total)
