# A diferencia de otros lenguajes, en python la variable no tiene un tipo definido y es practimente dinamica 
# Ejemplo java: int numero = 5; y en python: numero = 5

# Se puede usar '' o "" para definir una variable de tipo string, aunque es recomendable usar "" 
# para evitar problemas con las comillas simples dentro de una cadena de texto y para mejorar la legibilidad del codigo
#Variable de tipo String
#En python no se necesita ";" al final de cada linea, aunque se usar para escribir varias instrucciones en una sola linea, pero no es recomendable
Name= "Juan"
LastName= "Perez"
#Variable de tipo entero
Age=  30
number= 10
#Variable de tipo flotante, su uso es para representar numeros con decimales
Height = 1.75
Price_cell= 999.99
#Variable de tipo booleano, su uso es para representar valores de verdadero o falso
is_student = True
is_employed = False
#Varibl de tipo lista, su uso es para representar una coleccion de elementos, se pueden modificar y agregar elementos a la lista
fruits= ["manzana","banana","naranja"]
#Variable de tipo tupla, su uso es para representar una coleccion de elementos que no se pueden modificar, es decir, sonh inmutables
colors= ('rojo', 'verde', 'azul')


#Variable de tipo diccionario, su uso es para representar una coleccion de pares clave-valor, se pueden modificar y agregar elementos al diccionario
person={
    "name": "juan",
    "age": 30,
    "city": "madrid",
    "is_student": True,
    "hobbies": ["futbol", "musica", "cine"]
    
}


#Variable de tipo conjunto (set), su uso es para representar una coleccion de elementos unicos, no se pueden modificar pero si se pueden agregar elementos al conjunto
unique_numbers= {1,2,3,4,5}


#Variable de tipo None, su uso es para representar la ausencia de valor o un valor nulo
result = None   
#Variable de tipo bytes, su uso es para representar datos binarios, como archivos o datos de red
data = b'Hello, World!'

#variable de tipo bytearray, su uso es para representar datos binarios mutables, es decir, se pueden modificar los datos almacenados en el bytearray
mutable_data = bytearray(b'Hello, World!')
#Variable de tipo range, su uso es para representar una secuencia de numeros enteros, se puede usar para iterar sobre una secuencia de numeros en un bucle for
numbers = range(1, 10)

# iterar significa recorrer una secuencia de elementos, como una lista o un rango, y realizar una accion para cada elemento de la secuencia