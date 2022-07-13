# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:43:24 2022

@author: UPEU
"""

import sqlite3
conexion=sqlite3.connect("bdbiblioteca.db")
# Recordemos al insertar que el id es autoincrement
consulta=""" INSERT INTO
                PAIS(NOMBRE, ESTADO)
                VALUES('Brasil','A')
         """
cursor = conexion.cursor()
cursor.execute(consulta)

# Nunca olviden hacer commit.....
conexion.commit()
conexion.close()

         