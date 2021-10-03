# -*- coding: utf_8 -*-
import os
import random

import pandas

nombreArchivoCSV = "play_db.csv"

def limpiarPantalla():	
	if(os.name == "posix"):
		os.system("clear")
	elif(os.name == "ct" or os.name == "nt" or os.name == "dos"):
		os.system("cls")




#------------------------------------------------------------------------------------


print("Actividad 5.5")
print("Implementación del Algoritmo de Naïve-Bayes")

# Importar archivo CSV en un dataframe de pandas:

df = pandas.read_csv(nombreArchivoCSV)

print(df)







