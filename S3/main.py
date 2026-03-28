# Taller Semana 3 - Refactorización y Blindaje
# Este script implementa: Type Aliases, funciones puras con type hints,
# manejo de excepciones con raise/try/except.

from datetime import datetime
from typing import Dict, List

# Type Aliases: nombrar los tipos hace el código más legible y deja claro
# qué estructura de datos espera cada función.
Recuerdo = Dict[str, str]
MemoriaAgente = List[Recuerdo]


def login():
    # Definimos usuarios y contraseñas en el código
    admin_user = "admin"
    admin_pass = "admin123"
    invitado_user = "invitado"
    invitado_pass = "invitado"

    intentos = 0
    max_intentos = 3

    # Máximo 3 intentos antes de bloquear
    while intentos < max_intentos:
        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()

        if usuario == admin_user and contrasena == admin_pass:
            print("[OK] Acceso concedido como administrador.")
            return usuario, "admin"
        elif usuario == invitado_user and contrasena == invitado_pass:
            print("[OK] Acceso concedido como invitado.")
            return usuario, "invitado"
        else:
            intentos += 1
            print(f"[Error] Credenciales incorrectas. Intento {intentos} de {max_intentos}.")

    # Si se llega aquí, se agotaron los intentos
    print("[Alerta] Usuario bloqueado. Cerrando sistema.")
    return None, None


def comando_ping() -> str:
    """Responde con 'pong!' al comando ping.
    
    Returns:
        str: Mensaje de respuesta del sistema.
    """
    print("pong!")
    return "Se ha enviado un ping y de respuesta se devolvió un pong."


def contar_letras() -> str:
    """Cuenta vocales y consonantes de una frase ingresada por el usuario.
    
    Returns:
        str: Mensaje con el resultado del conteo.
    """
    frase = input("Ingresa una frase: ").lower()
    vocales = 'aeiou'
    cont_v = 0
    cont_c = 0
    
    for ch in frase:
        if ch.isalpha():
            if ch in vocales:
                cont_v += 1
            else:
                cont_c += 1
    
    print(f"Vocales: {cont_v} | Consonantes: {cont_c}")
    return f"Se solicitó el conteo de la frase. Vocales: {cont_v}, Consonantes: {cont_c}"


def comando_fecha_hoy(role: str) -> str:
    """Muestra la fecha y hora actual. Solo disponible para administradores.
    
    Args:
        role: Rol del usuario actual ('admin' o 'invitado').
    
    Returns:
        str: Mensaje con la fecha/hora o confirmación de acceso denegado.
        
    Raises:
        PermissionError: Si el usuario no tiene rol de administrador.
    """
    # raise lanza el error hacia arriba; el try/except del bucle principal lo atrapa (similar a un 403)
    if role != "admin":
        raise PermissionError("Privilegios insuficientes")
    
    hoy = datetime.now()
    print("Fecha y hora actual:", hoy.strftime('%Y-%m-%d %H:%M:%S'))
    return f"[PseudoAgente] La fecha y hora actual es: {hoy.strftime('%Y-%m-%d %H:%M:%S')}"


def validar_password(logged_username: str) -> str:
    """Valida una nueva contraseña propuesta según reglas de seguridad.
    
    Reglas:
    1. Longitud mínima de 8 caracteres
    2. No puede ser igual al nombre de usuario
    
    Args:
        logged_username: Nombre del usuario actual logueado.
    
    Returns:
        str: Mensaje indicando si la contraseña es válida o rechazada.
    """
    propuesta = input("Ingresa la nueva contraseña propuesta: ")
    
    if len(propuesta) < 8:
        print("[Rechazada] La contraseña debe tener al menos 8 caracteres.")
        return "[Rechazada] La contraseña debe tener al menos 8 caracteres."
    
    if propuesta == logged_username:
        print("[Rechazada] La contraseña no puede ser igual al nombre de usuario.")
        return "[Rechazada] La contraseña no puede ser igual al nombre de usuario."
    
    print("[OK] Contraseña válida (según las reglas del ejercicio).")
    return "[OK] Contraseña válida."


def calculadora() -> str:
    """Realiza operaciones aritméticas básicas (+, -, *, /).
    
    Solicita dos números y un operador al usuario, valida la entrada
    y realiza la operación correspondiente.
    
    Returns:
        str: Mensaje con el resultado de la operación.
    """
    while True:
        a_str = input("Ingresa el primer número: ").strip()
        try:
            a = float(a_str)
            break
        except ValueError:
            print("Entrada inválida. Debes ingresar un número. Intenta de nuevo.")

    valid_ops = ['+', '-', '*', '/']
    while True:
        op = input("Ingresa el operador (+, -, *, /): ").strip()
        if op in valid_ops:
            break
        print("Operador no válido. Ingresa uno de: +, -, *, /. Intenta nuevamente.")

    # Evitar división por cero antes de aceptar el segundo número
    while True:
        b_str = input("Ingresa el segundo número: ").strip()
        try:
            b = float(b_str)
            if op == '/' and b == 0:
                print("Operación no válida: división por cero. Ingresa otro número.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Debes ingresar un número. Intenta de nuevo.")

    # Realizamos la operación
    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        res = a / b

    # Mostrar resultado con limpieza simple
    if isinstance(res, float) and res.is_integer():
        print("Resultado:", int(res))
        return f"Se ejecutó la calculadora. Resultado: {int(res)}"
    else:
        print("Resultado:", res)
        return f"Se ejecutó la calculadora. Resultado: {res}"


def gestionar_historial(accion: str, memoria: MemoriaAgente, keyword: str = "") -> str:
    """Gestiona el historial del agente: mostrar todo, limpiar o buscar.
    
    Esta función es una Tool (Herramienta) pura que NO imprime nada,
    solo procesa datos y retorna el resultado. El bucle principal
    se encarga de imprimir lo que esta función retorna.
    
    Args:
        accion: Acción a realizar ('all', 'clear', o 'search').
        memoria: Historial actual del agente (MemoriaAgente).
        keyword: Palabra clave para buscar (solo si accion='search').
    
    Returns:
        str: Resultado formateado de la operación.
    """
    if accion == "all":
        if not memoria:
            return "[PseudoAgente] No hay registros en el historial."
        
        resultado = "[PseudoAgente] Mostrando todo el historial:\n"
        for i, e in enumerate(memoria, start=1):
            resultado += f"{i}. [{e.get('timestamp')}] {e.get('rol')}: {e.get('descripcion')}\n"
        return resultado.strip()
    
    elif accion == "clear":
        return "[PseudoAgente] Historial eliminado."
    
    elif accion == "search":
        found = []
        for entry in memoria:
            descripcion_lower = entry.get("descripcion", "").lower()
            if keyword.lower() in descripcion_lower:
                found.append(entry)
        
        if not found:
            return "[PseudoAgente] No encontré registros que coincidan con esa palabra."
        
        resultado = f"[PseudoAgente] Total de coincidencias: {len(found)}\n"
        for i, elem in enumerate(found, start=1):
            resultado += f"{i} >>> [{elem.get('timestamp')}] {elem.get('rol')}: {elem.get('descripcion')}\n"
        return resultado.strip()
    
    return "[PseudoAgente] Acción no reconocida."


def main():
    usuario, role = login()
    if usuario is None:
        return
    def print_menu():
        print("\n===== MENU =====")
        print("Opciones disponibles:")
        print(" - ping           : Responde 'pong!'")
        print(" - contar         : Cuenta vocales y consonantes")
        print(" - fecha_hoy      : Muestra fecha (solo admin)")
        print(" - validar_pass   : Valida una nueva contraseña propuesta")
        print(" - calculadora    : Realiza operaciones aritméticas")
        print(" - historial       : Buscar en historial (usa 'historial all' o 'historial clear')")
        print(" - salir          : Cierra el agente")
        print("=================")

    print_menu()
    # Inicializamos historial usando el Type Alias MemoriaAgente
    historial_chat: MemoriaAgente = [
        {"timestamp": "2026-03-18 13:50:51", "cmd": "ping", "rol": "invitado", "descripcion": "Se ha enviado un ping y de respuesta se devolvió un pong."},
        {"timestamp": "2026-03-18 13:50:56", "cmd": "fecha_hoy", "rol": "invitado", "descripcion": "[Acceso Denegado] Este comando requiere privilegios de administrador."}
    ]

    while True:
        cmd = input("-> ").strip().lower()
        mensaje = ""

        try:
            if cmd == "ping":
                mensaje = comando_ping()
                
            elif cmd == "contar":
                mensaje = contar_letras()
                
            elif cmd == "fecha_hoy":
                mensaje = comando_fecha_hoy(role)  # lanza PermissionError si es invitado
                
            elif cmd == "validar_pass":
                mensaje = validar_password(usuario)
                
            elif cmd == "calculadora":
                mensaje = calculadora()
                
            elif cmd.startswith("historial"):
                partes = cmd.split()
                if len(partes) > 1:
                    subcmd = partes[1]
                else:
                    subcmd = None

                if subcmd == "all":
                    resultado = gestionar_historial("all", historial_chat)
                    print(resultado)
                    mensaje = "[PseudoAgente] Mostrado historial completo."

                elif subcmd == "clear":
                    resultado = gestionar_historial("clear", historial_chat)
                    print(resultado)
                    historial_chat.clear()
                    mensaje = "[PseudoAgente] Historial eliminado."

                else:
                    keyword = input("Ingresa la palabra clave a buscar: ").strip()
                    resultado = gestionar_historial("search", historial_chat, keyword)
                    print(resultado)
                    mensaje = resultado

            elif cmd == "salir":
                mensaje = "Se ha solicitado terminar la sesión."
                d_log: Recuerdo = {"timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                         "cmd": cmd,
                         "rol": role,
                         "descripcion": mensaje}
                historial_chat.append(d_log)
                print("Apagando agente. ¡Hasta luego!")
                break
                
            else:
                print("Comando no reconocido. Intenta una de las opciones del menú.")
                mensaje = "Comando no reconocido."

        except PermissionError as e:
            print(f"[Acceso Denegado] {e}")
            mensaje = f"[Acceso Denegado] {e}"
            
        except ValueError as e:
            print(f"[Error] Entrada inválida: {e}")
            mensaje = f"[Error] Entrada inválida: {e}"

        # Guardamos la acción en el historial
        d_log: Recuerdo = {"timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                 "cmd": cmd,
                 "rol": role,
                 "descripcion": mensaje}
        historial_chat.append(d_log)

        # Volvemos a mostrar el menú
        print_menu()


if __name__ == "__main__":
    main()