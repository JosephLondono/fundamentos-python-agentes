# Fundamentos de python para Ingeniería de Agentes

- Horario: Lunes y Miércoles 1PM - 2PM
- Grupo asignado: G1

El contenido de la sesiones prácticas se subirá en ramas que representen cada semana, así como los talleres de la semana.

---

# Agencia de Agentes — Reto de Consolidacion

Reto de Consolidacion — Fundamentos de Python para Ingenieria de Agentes (Sofka).

Este proyecto une todo lo visto en Semana 4 (POO) y Semana 5 (SQLite + FastAPI) en un sistema
completo: la Agencia gestiona agentes, les asigna misiones, registra mensajes y consulta
informacion de paises del mundo para enriquecer el briefing de cada operativo.

---

## Como instalar y ejecutar

### 1. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv

# Windows
venv\Scripts\pip install -r requirements.txt

# Mac / Linux
venv/bin/pip install -r requirements.txt
```

### 2. Configurar variables de entorno

```bash
# Copia el archivo de ejemplo
cp .env.example .env

# Abre .env y llena los valores reales:
# AGENCIA_API_KEY=tu_clave_secreta
# EXTERNAL_API_URL=https://restcountries.com/v3.1
# DB_PATH=agentes.db
```

### 3. Poblar la base de datos con datos de ejemplo (solo la primera vez)

```bash
# Windows
venv\Scripts\python seed.py

# Mac / Linux
venv/bin/python seed.py
```

### 4. Levantar el servidor

```bash
# Windows
venv\Scripts\uvicorn main:app --reload

# Mac / Linux
venv/bin/uvicorn main:app --reload
```

El servidor queda disponible en: http://localhost:8000  
Documentacion interactiva (Swagger UI): http://localhost:8000/docs

### 5. Correr el cliente de demostracion (con el servidor andando)

```bash
# Windows
venv\Scripts\python cliente.py

# Mac / Linux
venv/bin/python cliente.py
```

---

## Tabla de endpoints

| Metodo | Ruta                          | Protegido | Descripcion                                                   |
|--------|-------------------------------|-----------|---------------------------------------------------------------|
| GET    | `/`                           | No        | Health check: verifica que el servidor esta vivo              |
| GET    | `/agentes/`                   | No        | Lista todos los agentes registrados                           |
| GET    | `/agente/{nombre}`            | No        | Devuelve los datos de un agente por nombre                    |
| POST   | `/agentes/`                   | Si        | Crea un agente nuevo                                          |
| POST   | `/mensajes/`                  | No        | Envia un mensaje de un agente a otro                          |
| GET    | `/mensajes/{nombre}`          | No        | Lee la bandeja de entrada de un agente                        |
| POST   | `/misiones/`                  | Si        | Crea una mision nueva asignada a un agente existente          |
| GET    | `/misiones/{id}`              | No        | Devuelve los detalles de una mision por ID                    |
| GET    | `/agente/{nombre}/misiones`   | No        | Lista todas las misiones de un agente                         |
| POST   | `/misiones/{id}/completar`    | Si        | Completa una mision y descuenta energia al agente             |
| GET    | `/briefing/{nombre}`          | No        | Datos del agente + info de pais de operaciones (API externa)  |

Los endpoints **protegidos** requieren el header `X-API-KEY` con la clave configurada en `.env`.
Sin el header o con clave incorrecta responden `401 Unauthorized`.

---

## Decisiones de Ingenieria

### 1. Esquema de la tabla `misiones`

Ademas de las columnas minimas del enunciado, agregue dos columnas extra:

- **`prioridad`** (`alta` / `media` / `baja`): en una agencia real no todas las misiones tienen
  el mismo nivel de urgencia. Tener prioridad en la DB permite filtrarlo despues o mostrarlo en
  el briefing sin tener que agregar logica fuera de la base de datos.

- **`creado_por`**: guarda quien creo la mision (puede ser el nombre de un operador o "sistema").
  Esto es trazabilidad basica: si una mision se crea mal, se puede saber quien la ordeno.
  En produccion esto seria el usuario autenticado del sistema de backoffice.

### 2. API publica elegida: Rest Countries (restcountries.com)

Elegí la API de paises porque encaja perfectamente con la narrativa de agentes que operan
en el mundo real. El endpoint `GET /briefing/{nombre}` consulta paises de la region Americas
y asigna uno aleatoriamente como "zona de operaciones" del agente: capital, region, poblacion
y bandera. Esto hace al briefing mucho mas inmersivo que un perfil plano, y la API es publica,
gratuita y sin autenticacion (perfecta para este ejercicio).

Endpoint usado: `/v3.1/region/americas?fields=name,capital,flags,region,population`

### 3. Estrategia de resiliencia ante falla de API externa

Si la API de paises falla o tarda, el servidor NO se cuelga. El plan es:

- **Timeout de 3 segundos**: si restcountries no responde en 3 segundos, cortamos la conexion.
- **try/except separado**: capturamos `Timeout`, `ConnectionError` y cualquier otro error de forma
  independiente para poder logear el motivo exacto con `logger.warning`.
- **Fallback**: el endpoint responde igualmente con los datos locales del agente, pero con
  `"fuente_externa": "no disponible (timeout)"` o `"no disponible (sin conexion)"` segun el caso.

Esto significa que un problema de red NUNCA rompe el briefing. El agente siempre tiene respuesta.

---

## Referencias consultadas

- FastAPI — Dependencies: https://fastapi.tiangolo.com/tutorial/dependencies/
- FastAPI — Header parameters: https://fastapi.tiangolo.com/tutorial/header-params/
- python-dotenv: https://pypi.org/project/python-dotenv/
- os.getenv: https://docs.python.org/3/library/os.html#os.getenv
- Python logging — basicConfig: https://docs.python.org/3/library/logging.html#logging.basicConfig
- requests — timeout: https://requests.readthedocs.io/en/latest/user/advanced/#timeouts
- Rest Countries API: https://restcountries.com/
- SQLite3 — Python docs: https://docs.python.org/3/library/sqlite3.html
