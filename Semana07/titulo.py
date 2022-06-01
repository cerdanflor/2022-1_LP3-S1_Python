# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:36:38 2022

@author: UPEU
"""
# Importamos la librería

import camelcase

# Tenemos una cadena llamada nombre y se desea 
# que se muestre en formato título
nombre = "flor elizabeth Cerdán león"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam
cam= camelcase.CamelCase()
print("Con camelcase....")

# Imprimimos el nombre en formato título
#Utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto cam2
# Al definir el objeto, incluimos los argumentos
# 'flor' y 'león'

cam2=camelcase.CamelCase('flor','león')
print(cam2.hump(nombre))