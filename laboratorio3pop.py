#Usamos recursión con memorización para calcular números fibonacci
#Ejercicio 1
def fibonacci (n,memo={}):
    if n in memo:
        return memo[n]
    if n <=1:
        return n
    memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo)
    return memo[n]
resultado=fibonacci(50)
print("Fibonacci de 50 es: ", resultado)

#Ejercicio 2
from decimal import Decimal, getcontext
getcontext().prec=50
numero1 = Decimal('1.123456789123456789')
numero2 = Decimal('2.987654321987654321')
resultado = numero1*numero2

print(f"resulado preciso: {resultado}")

#Ejercicio 3
import re
cadena = "ESTO es un EJEMPLO de uso AVANZADO de CADENAS y expresiones REGULARES."
patron = r'\b[A-Z]{2,}\b'
palabras_masyusculas = re.findall(patron,cadena)

print("palabras en mayuscula:",palabras_masyusculas)

#Ejercicio 4

a = True
b = False
c = True

resultado = (a and b) or (a and c) ^ b
print("Resulado de la operación lógica compleja: ", resultado)

#Ejercicio 5 

def sumar_o_default(a,b):
    return(a or 0) + (b or 0)

print(sumar_o_default(5,None))
print(sumar_o_default(None, None))
print(sumar_o_default(10,20))









