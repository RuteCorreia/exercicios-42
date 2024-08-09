#!/usr/bin/env python3
import getpass

Senha = "Python is awesome"

senhaDigitada = getpass.getpass("password: ")

if senhaDigitada == Senha:
    print("ACCESS GRANTED")
else: 
    print("ACCESS DENIED")    