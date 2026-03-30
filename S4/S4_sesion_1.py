import datetime

#Día 1: POO in a nutshell
## Clases: Instancias de objetos
## Objetos: Representaciones a partir de una clase
## Constructor: __init__
## self, siempre va con el constructor, self.attribute después. Es un tema entender el propósito de self
### En resumen: self funciona como un indicador de sitio, para saber a donde debes ir cuando utilizas las 
# funciones de una clase o accedes a los atributos
## No existen modificadores de acceso (public/private/protected) pero 
# existe el "_" para hacer ._attribute: Uso interno

#TO - DO: Construir una clase PseudoAgente
##Atributos de entrada: nombre
##Atributos adicionales: bateria, historial_chat
###Métodos/Funciones
#registrar_log()
#gestionar_historial
type Historial = dict[str, str]

def login(user: str, passwrd: str) -> dict[str]:
    if user == "admin" and passwrd == "admin123":
        return {
            "rol": user,
            "access": True,
            "descripcion": "[Sistema] Acceso concedido. Privilegios de Administrador activados.",
        }

    if user == "invitado" and passwrd == "1234":
        return {
            "rol": user,
            "access": True,
            "descripcion": "[Sistema] Acceso concedido. Modo Invitado.",
        }
def historial_sing(L_hist, op: str="all"):
    if op == "all":
        return {"result":L_hist, "mensaje": f"[PseudoAgente] Se mostró el historial actual hasta las {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} " }

    if op == "clear":
        return {"result":[], "mensaje": f"[PseudoAgente] Se borró el historial actual a las {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} " }
intentos = 0
rol_actual = ""
tiene_acceso = False

while intentos < 3 and not tiene_acceso:
    usuario = input("Usuario: ").strip().lower()
    password = input("Contraseña: ").strip()

    login_attempt = login(usuario, password)
    rol_actual = login_attempt["rol"]
    tiene_acceso = login_attempt["access"]

    if not tiene_acceso:
        intentos += 1
        print(f"[Error] Credenciales incorrectas. Te quedan {3 - intentos} intentos.")
    else:
        print(login_attempt["descripcion"])


## Pseudoagente
if tiene_acceso:    
    historial_chat: list[Historial] = [] 
    #{'timestamp': '2026-03-18 13:50:51', 'cmd': 'ping', 'rol': 'invitado', 'descripcion': 'Se ha enviado un ping y de respuesta se devolvió un pong.'}, {'timestamp': '2026-03-18 13:50:56', 'cmd': 'fecha_hoy', 'rol': 'invitado', 'descripcion': '[Acceso Denegado] Este comando requiere privilegios de administrador.'}, {'timestamp': '2026-03-18 13:51:02', 'cmd': 'dormir', 'rol': 'invitado', 'descripcion': 'Comando no existe. Intente de nuevo'}, {'timestamp': '2026-03-18 13:51:07', 'cmd': 'salir', 'rol': 'invitado', 'descripcion': 'Se ha solicitado terminar la sesión.'}
    pseudo_activo = True
    mensaje = ""

    while pseudo_activo:
        cmd = input(f"\n{usuario}@PseudoAgente>: ").strip().lower()

        if cmd == "salir":
            print("[PseudoAgente] Apagando sistemas...")
            pseudo_activo = False
            mensaje = "Se ha solicitado terminar la sesión."
        elif cmd == "ping":
            print("pong~")
            mensaje = "Se ha enviado un ping y de respuesta se devolvió un pong."            
        
        elif cmd.startswith("hist"):
            if " " in cmd:
                sing = cmd.split(" ")[-1]
                hist_result = historial_sing(historial_chat, sing)
                historial_chat = hist_result["result"]
                print(hist_result["mensaje"])
                print(historial_chat)

            else:
                found = []
                word = input("Ingresa la palabra clave a buscar: ").lower()
                for i, elem in enumerate(historial_chat):
                    if(word in elem["descripcion"]):
                        found.append(elem)
                        #found.append(historial_chat[i])
                mensaje = f" [PseudoAgente] Total de concidencias: {len(found)}"
                print(mensaje)
                if len(found) > 0:                    
                    for i, elem in enumerate(found):
                        print(f"{i+1} >>> {elem}")
                else:
                    print("[PseudoAgente] No encontré registros que coincidan con esa palabra.")

        else:
            mensaje = " [PseudoAgente] Comando no existe. Intente de nuevo"
            print(mensaje)

        #Uso del type Historial
        d_log: Historial = {"timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "cmd": cmd,
                "rol": rol_actual,
                "descripcion": mensaje}
        
        historial_chat.append(d_log)
        

else:
    print("Acceso denegado.")