#Dia 2 - Estructuras de control
## while 

#nombre = input("¿Cómo te llamas?: ")
#print(f"Hola, {nombre}. Adios~")

#Estructura y lógica: while
## while condicion:
#   ...
#   ...
#   if(...):
#        break
##  Cuidado con los bucles infinitos! El truco? La 'actualización/gestión' de la condición
##  break, continue

#Previa del taller de la semana (Mini-taller II): Hacer un pseudoagente estilo consola
## ¿Qué podra hacer este agente por medio de comandos?
### Terminar la sesión - salir
### Responder un ping con un pong - ping
### Contar letras en una palabra: Total, vocales y consonantes - contar

print("----- Iniciando el pseudoagente estilo consola -------")

#Banderas/Banderines - Booleanos 

sistema_activo = True
while sistema_activo:
    cmd = input("Agente>: ").lower()

    if cmd == "salir":
        print("------Agente apagado. Vuelve pronto.------")
        sistema_activo = False
    elif cmd == "ping":
        print("pong.")
    elif cmd =="contar":
        palabra = input("Ingrese una palabra: ").lower()
        tot_letras = len(palabra)
        tot_vocales = 0
        tot_cons = 0
        
        for p in palabra:
            if p in "aeiou":
                tot_vocales +=1
            else:
                tot_cons +=1
        
        print(f"Palabra ingresada: {palabra}")
        print(f"Total de vocales: {tot_vocales}")
        print(f"Total de consonantes: {tot_cons}")
        print(f"Total de letras: {tot_letras}")
    

    else:
        print("------Comando desconocido. Intente de nuevo.-------")