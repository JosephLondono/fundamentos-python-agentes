# Taller Semana 1 - Agente con Login y comandos
# Este script implementa: Login con 3 intentos, comandos base,
# y tres comandos nuevos: fecha_hoy (solo admin), validar_pass, calculadora.

from datetime import datetime


def login():
    # Definimos usuarios y contraseñas en el código
    admin_user = "admin"
    admin_pass = "admin123"
    invitado_user = "invitado"
    invitado_pass = "invitado"

    intentos = 0
    max_intentos = 3

    # Explicación del control de intentos:
    # Usamos un contador `intentos` que aumentamos en cada fallo. Si llega
    # a `max_intentos` (3) salimos del loop y bloqueamos el acceso.
    # Esto evita intentos infinitos y permite informar al usuario.
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


def comando_ping():
    print("pong!")


def comando_contar():
    frase = input("Ingresa una frase: ").lower()
    vocales = 'aeiou'
    cont_v = 0
    cont_c = 0
    # Recorremos cada carácter de la frase.
    # 'ch' es una abreviatura de 'character' (carácter) y se usa comúnmente
    # en ejemplos cortos para representar el elemento actual en la iteración.
    # `isalpha()` es un método de strings que devuelve True si el carácter
    # es una letra (A-Z o a-z). Lo usamos para evitar contar espacios,
    # números o signos de puntuación como consonantes.
    for ch in frase:
        if ch.isalpha():
            if ch in vocales:
                cont_v += 1
            else:
                cont_c += 1
    print(f"Vocales: {cont_v} | Consonantes: {cont_c}")


def comando_fecha_hoy(role):
    if role != "admin":
        print("[Acceso Denegado] Este comando requiere privilegios de administrador.")
        return
    hoy = datetime.now()
    print("Fecha y hora actual:", hoy.strftime('%Y-%m-%d %H:%M:%S'))


def comando_validar_pass(logged_username):
    propuesta = input("Ingresa la nueva contraseña propuesta: ")
    # Validaciones requeridas:
    # 1) Longitud mínima 8
    # 2) No debe ser igual al nombre de usuario con el que se ha logueado
    if len(propuesta) < 8:
        print("[Rechazada] La contraseña debe tener al menos 8 caracteres.")
        return
    if propuesta == logged_username:
        print("[Rechazada] La contraseña no puede ser igual al nombre de usuario.")
        return
    print("[OK] Contraseña válida (según las reglas del ejercicio).")


def comando_calculadora():
    # Nota de por qué convertimos a float/int:
    # Inputs desde `input()` vienen como texto (str). Para realizar operaciones
    # matemáticas necesitamos convertirlos a `int` o `float`. Si no lo hiciéramos,
    # el operador `+` concatenaría strings en lugar de sumar números.
    # Mejor experiencia: si el usuario se equivoca se le pide reingresar sin
    # salir al menú principal. Reintentamos para cada input hasta que sea válido.
    # Pedimos el primer número
    while True:
        a_str = input("Ingresa el primer número: ").strip()
        try:
            a = float(a_str)
            break
        except ValueError:
            print("Entrada inválida. Debes ingresar un número. Intenta de nuevo.")

    # Pedimos el operador y validamos
    valid_ops = ['+', '-', '*', '/']
    while True:
        op = input("Ingresa el operador (+, -, *, /): ").strip()
        if op in valid_ops:
            break
        print("Operador no válido. Ingresa uno de: +, -, *, /. Intenta nuevamente.")

    # Pedimos el segundo número; si el operador es división, evitamos cero
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
    else:
        print("Resultado:", res)


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
        print(" - salir          : Cierra el agente")
        print("=================")

    print_menu()
    while True:
        cmd = input("-> ").strip().lower()
        if cmd == "ping":
            comando_ping()
        elif cmd == "contar":
            comando_contar()
        elif cmd == "fecha_hoy":
            comando_fecha_hoy(role)
        elif cmd == "validar_pass":
            comando_validar_pass(usuario)
        elif cmd == "calculadora":
            comando_calculadora()
        elif cmd == "salir":
            print("Apagando agente. ¡Hasta luego!")
            break
        else:
            print("Comando no reconocido. Intenta una de las opciones del menú.")

        # Después de ejecutar el comando o ante entrada inválida, mostramos
        # nuevamente el menú para que el usuario vea las opciones.
        print_menu()


if __name__ == "__main__":
    main()
