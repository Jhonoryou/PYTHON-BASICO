# bucles
""" En python existen 3 tipos de bucles: """
# 1. for
# 2. while
# 3. do-while

# for
# El bucle for se utiliza para iterar sobre una secuencia de elementos, como una lista, tupla, diccionario, conjunto o cualquier otro tipo de iterable
# La sintaxis del bucle for es la siguiente:
# for variable in iterable:
#     bloque de codigo

# Ejemplo de bucle for para iterar sobre una lista de frutas
fruits = ["manzana", "banana", "pera", "naranja"]

for fruit in fruits:
    print("La fruta es:",fruit)
    
#Ejemplo de bucle for para iterar sobre un rango de numeros
# range(1, 11) = inicia en 1 y termina ANTES de 11, por eso itera del 1 al 10
# i es la variable que toma el valor de cada numero en cada iteracion del bucle
for i in range(1,11):
    print("El numero es:", i)
    
#Ejemplo de bucle for para iterar sobre un diccionario
#Definimos un diccionario con los nombre de los estudiantes y sus edades

students ={
    "Juan":20,
    "Maria":22,
    "Pedro":10,
    "Ana": 18,
    "Luis": 25,
    "Sofia":30
}   

#Primero se define la variable student que tomara el valor de cada clave del diccionario en cada iteracion del bucle
#Luego se imprime el nombre del estudiante y su edad utlizando la variable student para acceder al valor de la clave
#En cada iteracion del bucle, la variable student tomara el valor de cada clave del diccionario, es decir, el nombre de cada estudiante y su edad
for student in students:
    print("El nombre del estudiante es:", student, " y su edad es:", students[student])


#ejemplo de bucle for para iterar sobre un conjunto
#Definimos un conjunto con los nombres de los colores
colors ={ "rojo", "verde", "rosa"}

#ITERAR CON EL BUCLE FOR SOBRE UN CONJUNTO
for color in colors:
    print("El color es:", color)