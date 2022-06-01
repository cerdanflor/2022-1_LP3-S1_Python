# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:57:26 2022

@author: UPEU
"""

archivo = open("noticia.txt","at")
#\n es para agregar el contenido en una línea final
contenido="\nFuente: RPP"

archivo.write(contenido)
archivo.close()