# uso del print( ) para mostrar informacion en la consola, se pueden imprimir variables, texto o una combinacion de ambas
# se pueden usar comillas simples o dobles para definir una cadena de texto, aunque es recomendable usar comillas dobles para evitar problemas con las comillas simples dentro de la cadena de texto
number= 10
number2=20
print("El primer numero es:", number)

print("El segundo numero es :", number2)

suma= number + number2
print("La suma de los numeros es:", suma)

# Se puede imprimir variables de diferentes tipos, como enteros, flotantes, booleanos,listas, tuplas, diccionarios, conjuntos, None, bytes y bytearray,etc
fruits= ["manzana","banana","naranja"]
print("la primera fruta es:", fruits[0])
print("la segunda fruta es:", fruits[1])
print("la tercera fruta es:", fruits[2])

# Imprimir todo el conjunto de frutas
print("Las frutas son:", fruits)

# Se pueden imprimir variables de tipo diccionario, mostrando las claves y los valores
person={
    "name": "juan",
    "age": 30,
    "city": "madrid",
    "is_student": True,
    "hobbies": ["futbol", "musica", "cine"]
    
}

print("El nombre de la persona es:", person["name"])
print("La edad de la persona es:", person["age"])
print("La ciudad de la persona es:", person["city"])
print("¿Es estudiante?", person["is_student"])
print("Los hobbies de la personas son", person["hobbies"])

print("---------------------------------")
# Uso de \n para imprimir en varias lineas, se puede usar para mejorar la legibilidad del codigo
print("El nombre de la persona es:", person["name"], "\n La edad de la persona es:", person["age"], "\n La ciudad de la persona es:", person["city"], "\n ¿Es estudiante?", person["is_student"], "\n Los hobbies de la personas son", person["hobbies"])
# uso de f-strings para imprimir variables de una manera mas legible y facil de entender, se pueden usar para mejorar la legibilidad del codigo
print(f"El nombre de la persona es: {person['name']} \n La edad de la persona es: {person['age']} \n La ciudad de la persona es: {person['city']} \n ¿Es estudiante? {person['is_student']} \n Los hobbies de la personas son: {person['hobbies']}")
