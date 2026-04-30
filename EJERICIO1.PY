#EJERICIO UNO CREA UNA CALCULADORA SUMA, RESTA, MULTIPLICACION Y DIVISION DONDE APLIQUES LO APRENDIDO DE DE LA CLASE VARIABLES Y INGRESAR DAOTS Y PRINT

a= float(input("Ingrese el primer numero: \n"))
b= float(input("Ingrese el segundo numero: \n"))

suma =a+b
resta = a-b
multiplicacion= a*b
division= a/b


#salida de datos en la pantalla usando print
print("La suma de: "+ str (a)+ " y "+ str(b) + " es: " + str(suma)) 
#No se puede concatenar un numero con una cadena de texto, por lo que se debe convertir el numero a una cadena de texto usando la funcion str() para poder concatenarlo con el texto y mostrarlo en la pantalla
print("La resta de", a, " y ", b, "es:", resta)
#Si se puede concatenar un numero con una cadena de texto usando la comas, ya que la funcion print() se encarga de convertirlo en el formato adecuado para mostrarlo en pantalla

print("La multiplicacion de: " + str (a) + " y " +str(b) + " es: " + str (multiplicacion) )
print("La division de: ", a , " y ", b, " es: ", division)

# EN la salida de print solo se permite usar el simbolo de suma para
# concatenar cadena de texto, pero no se puede usar para concatenar numero por lo que es necesario convertilo en cadena de texto 