#!/usr/bin/env python3

idade = input("Please tell me your age ")

if not idade.isdigit():
   print("Digite apenas numeros!")
else:
    print("You are currently " f" {int(idade) } "" years old.")
    print("In 10 years, you'll be: " f" {int(idade) + 10} ""years old.")
    print("In 20 years, you'll be: " f" {int(idade) + 20} ""years old.")
    print("In 30 years, you'll be: " f" {int(idade) + 30} ""years old.")