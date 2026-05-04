#INGRESAR DATOS EN PYTHON HACEMOS USO DE LA FUNCION INPUT PARA INGRESAR DATOS DESDE EL TECLADO

#Con el metodo input se definira el tipo de variable a ingresar, por ejemplo, si queremos ingresar un numero entero, usaremos int(input()), si queremos ingresar un numero flotante, usaremos float(input()), y si queremos ingresar una cadena de texto, usaremos str(input()) o simplemente input() ya que por defecto el tipo de dato ingresado es una cadena de texto (string)
#Primero definirmos las variables donde se almacenaran los datos ingresados por el usuario, luego usaremos la funcion input para solicitar al usuario que ingrese los datos y almacenarlos en las variables correspondientes, finalmente podemos imprimir los datos ingresados por el usuario para verificar que se han almacenado correctamente
name = input("Ingrese su nombre:")

#MOSTRAR EN PATALLA EL NOMBRE INGRESADO POR EL USUARIO POR LA FUNCION PRINT
print("El nombre ingresado es:", name)

#Ingresar un numero entero
age = int(input("Ingrese su edad:"))

#Mostrar en pantalla la edad ingresada por el usuario
print("La edad ingresada es:", age)
#Ingresar un numero flotante
height = float(input("Ingrese su altura en metros:"))
#Mostrar en pantalla la altura ingresada por el usuario
print("La altura ingresada es:", height)        


#ingresar un numero bites, se puede usar para representar datos binarios, como archivos o datos de red
data = input("Ingrese un dato en formato bytes:")
#Convertir el dato ingresado a bytes y almacenarlo en la variable data_bytes
data_bytes = data.encode('utf-8')
#Mostrar en pantalla el dato ingresado por el usuario en formato bytes  
print("El dato ingresado en formato bytes es:", data_bytes)

#ingresar un datos en formato bytearray, se puede usar para representar datos binarios mutables, es decir, se puede modificar los datos almacenados 
#en el bytearray
mutable_data_input = input("Ingrese un dato en formato bytearray:")
#Convertir el dato ingresado a bytearray y almacenarlo en la variable mutable_data  
mutable_data = bytearray(mutable_data_input.encode('utf-8'))



# EXITEN TIPO DE DATOS PRIMITIVOS Y COMPUESTOS, LOS PRIMITIVOS SON LOS QUE NO PUEDEN SER DIVIDIDOS EN PARTES MAS PEQUEÑAS, 
# COMO LOS NUMERO ENTEROS, FLOTANTES, 
# BOOLEANOS Y LOS COMPUESTOS SON LOS QUE PUEDEN SER DIVIDIDOS EN PARTES MAS PEQUEÑAS, COMO LAS LISTAS, TUPLAS, DICCIONARIOS, CONJUNTOS,ETC.

# Existen dos formas de comentar en python, los comentarios de una sola linea se hacen con el simbolo # y los comentarios de varias lineas se hacen con 
# """ o con ''' para encerrar el bloque de texto que se desea comentar, aunque es recomendable usar """ para los comentarios de varias lineas
# ya que es mas legible y facil 
# de entender.



