# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:15:53 2022

@author: UPEU
"""

try:
    numerador = float(input("Numerador: "))
    denominador = float(input("Denominador: "))
    resultado =numerador/denominador
    print(f"Resultado = {resultado}")
    print("Gracias")
except ZeroDivisionError:
    print("No puedes dividir entre CERO....")
except:
    print("Hubo un error")
else:
    print("La división se realizó correctamente")
finally:
    print("La operación terminó")