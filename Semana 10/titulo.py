# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:55:04 2022

@author: UPEU
"""

# Problema: Necesitamos mostrar los nombres de una cadena
# presentando las primeras letras en mayúscula
# En word se conoce como Fornato Título

# Importar la librería

import camelcase

nombre="flor elizabeth cerdán león"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam

cam=camelcase.CamelCase()
print("Con camelcase.....")

# Imprimimos el nombre en formato titulo
# Utilizamos camelcase

print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto llamado cam2
# Al definir el objeto, incluimos los argumentos
# 'flor' y 'león'

cam2=camelcase.CamelCase('flor','león')
print(cam2.hump(nombre))