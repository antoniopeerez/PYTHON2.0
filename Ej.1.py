#Crea una aplicación que pida un número y calcule su factorial 
from math import factorial


factorial = 1
numero = int(input("Introduce el numero para calcular su factorial: "))

if numero<0:
   print("No existe factorial de un numero negativo")
else:
    for i in range(2,(numero + 1)):
       factorial = factorial * i
print("El factorial de ", numero, "es", factorial)