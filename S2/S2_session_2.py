import datetime
print("-----------Iniciando el pseudoagente estilo consola--------------------")

##Login

intentos = 0
rol_actual = ""
tiene_acceso = False

while intentos < 3 and not tiene_acceso:
    usuario = input("Usuario: ").strip().lower()
    password = input("Contraseña: ").strip()
    
    if usuario == "admin" and password == "admin123":
        rol_actual = "admin"
        tiene_acceso = True
        print("[Sistema] Acceso concedido. Privilegios de Administrador activados.")
        
    elif usuario == "invitado" and password == "1234":
        rol_actual = "invitado"
        tiene_acceso = True
        print("[Sistema] Acceso concedido. Modo Invitado.")
        
    else:
        intentos += 1
        print(f"[Error] Credenciales incorrectas. Te quedan {3 - intentos} intentos.")

## Pseudoagente
if tiene_acceso:
   
    #TO-DO: Agregar una memoria al pseudo agente utilizando listas y diccionarios
    #historial_chat=[]
    pseudo_activo = True
    mensaje = ""
    while pseudo_activo:
        #TO-DO: Activar/Desactivar memoria del agente
        #....
        #Ahora, cada vez que se interactúe con el pseudoagente hay que tener 
        # en cuenta el guardado de las interacciones en historial_chat
        cmd = input(f"\n{usuario}@PseudoAgente>: ").strip().lower() 
        
    if cmd == "salir":
        print("[PseudoAgente] Apagando sistemas...")
        sistema_activo = False
        #mensaje
    #TO-DO: Habilitar una opción para activar y desactivar la memoria
    elif cmd == "ping":
        print("pong~")
        #mensaje
        
    elif cmd == "contar":
        pal = input("Ingrese una palabra: ").strip().lower()
        tot_letras = len(pal)
        tot_vocales = 0
        tot_cons = 0
        for p in pal:
            if p in "aeiou":
                tot_vocales += 1
            elif p.isalpha(): 
                tot_cons += 1
                
        print(f"Palabra ingresada: {pal}")
        print(f"Total de vocales: {tot_vocales}")
        print(f"Total de consonantes: {tot_cons}")
        print(f"Total de letras: {tot_letras}")
        #mensaje
    elif cmd == "fecha_hoy":
        if rol_actual == "admin":
            ahora = datetime.datetime.now()
            print(f"[PseudoAgente] La fecha y hora actual es: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("[Acceso Denegado] Este comando requiere privilegios de administrador.")
        #mensaje
    elif cmd == "validar_pass":
        print("Validar pass")
        #mensaje
    elif cmd == "calculadora":
        print("Calculadora")
        #mensaje
    #TO-DO: Tener en cuenta el valor de memoria activa para saber si se guarda o no.

    #TO-DO: Taller de la semana - Búsqueda de memoria
    d_logs = {"timestamp": datetime.datetime.now(),
              "cmd": cmd,
              "rol": rol_actual,
              "descripcion": mensaje}

else:
    print("Acceso denegado.")
