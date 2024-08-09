#!/usr/bin/env python3
numero1 = int(input("Enter the first number:: "))
numero2 = int(input("Enter the second number: "))

Resultado = numero1 * numero2

print(numero1, "*",numero2,"=", Resultado) 

if Resultado > 0:
    input("The result is positive.")
elif Resultado < 0:
    input("The result is negative.")    
elif Resultado == 0:   
    input("The result is positive and negative.")    