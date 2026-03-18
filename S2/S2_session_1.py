##Temas de la semana
## Día 1 - Listas y Diccionarios 
### Listas: [ ] Objeto mutable 
# - index (índice | posicionamiento) >>> str
notas = [80, 65, 60, 96, 74, 45]

#variedad = [80, "Celular", True, 45.4]

nombre = "Mishell"
# 0 - 80, 1 - 65 .... 5 - 45
# -1 ~ 45, -2 ~ 47 .... -6 ~ 80 
#Total de elementos lista 'notas': 6
#print(f"Total de elementos: {len(notas)}")
#print(f"Nombre: {nombre} ")
#print(f"Primera letra: {nombre[0]}")
#print(f"Ultimo elemento: {notas[-1]}")

#Funciones típicas para listas
#append(): Agregar un elemento a la lista
#print(notas)
#notas.append(90)
#print(notas)

notas_2 = [98, 55, 60]

#print(f"Concatenación de listas: {notas + notas_2}") #Concatenación
#print(notas)
#extend
#notas.extend(notas_2)
#print(f"Concatenación de listas pero con extend: {notas}")

#TO-DO: Tarea autónoma - 
# ¿Cómo agregar elementos a una lista en una posición en concreto? 
# ¿Qué otras funciones hay para usar con listas?
# ¿Cómo ordenamos una lista? Ascendente, Descendente.


### Diccionarios: { } - Par clave, valor - Mutable

estudiantes = {"M14531": "Mishell Yagual Mendoza", "M14986": "Maria José Castro"}
calificaciones = {"M14531": [98, 55, 60], "M14986": [74, 56, 86] }

#print(f"Acceder a un valor: {calificaciones['M14531']}")
# .get(clave)
#print(f"Acceder a un valor: {calificaciones.get('M14531')}")
# .update(dict)
#estudiantes.update({"M12598": "Caroline Alvarado"})
#print(estudiantes)
# TO - DO: .pop(), .keys(), .values()

#for
for key,value in estudiantes.items(): #[(A,B),(C,D)]
    print(f"Matrícula: {key} | Nombre: {value}")