# -*- coding: utf_8 -*-
import os
import random
import math
import pandas

nombreArchivoCSV = "play_db.csv"
nombreClase = "Play"
porcentajeEntrenamiento = 70

ConjuntoEntrenamiento = pandas.DataFrame()
ConjuntoPrueba = pandas.DataFrame()

# ConjuntoInicial = 

def limpiarPantalla():	
	if(os.name == "posix"):
		os.system("clear")
	elif(os.name == "ct" or os.name == "nt" or os.name == "dos"):
		os.system("cls")

def separarConjuntoEnEntrenamientoYPrueba(conjuntoI, conjuntoE, conjuntoP, porcentajeE):
	listaIndicesAleatorios = []
	numeroDeInstancias = len(conjuntoI.index)
	numeroDeInstanciasEntrenamiento = numeroDeInstancias * porcentajeE/100
	print("instancias de entrenamiento: ", numeroDeInstanciasEntrenamiento)
	k = 0
	while len(listaIndicesAleatorios) < numeroDeInstanciasEntrenamiento:
		num = random.randint(0,numeroDeInstancias-1)
		print(num, " está en la lista?: ",num in listaIndicesAleatorios)
		if num not in listaIndicesAleatorios:
			listaIndicesAleatorios.append(num)
	print(listaIndicesAleatorios)
	conjuntoE = conjuntoI.iloc[listaIndicesAleatorios]
	conjuntoP = conjuntoI.iloc[listaIndicesAleatorios]
	print(conjuntoE)
	return


	
	



#------------------------------------------------------------------------------------


print("\nActividad 5.5")
print("Implementación del Algoritmo de Naïve-Bayes\n")

# Importar archivo CSV en un dataframe de pandas:

print("Cargando Conjunto de Datos desde ", nombreArchivoCSV, "...")
ConjuntoInicial = pandas.read_csv(nombreArchivoCSV)
df = ConjuntoInicial


print("CSV cargado")

print("Conjunto de Datos: \n")

print(ConjuntoInicial)
print("\n")

# print("Conjunto de Datos filtrados: \n")

# print(df[["Windy", "Play"]])

# print(df[df["Play"] == "Yes"])


#ConjuntoEntrenamiento

# separarConjuntoEnEntrenamientoYPrueba(ConjuntoInicial, ConjuntoEntrenamiento, ConjuntoPrueba, porcentajeEntrenamiento)


listaIndicesAleatorios = []
numeroDeInstancias = len(ConjuntoInicial.index)
numeroDeInstanciasEntrenamiento = math.ceil(numeroDeInstancias * porcentajeEntrenamiento/100)
#print("instancias de entrenamiento: ", numeroDeInstanciasEntrenamiento)
k = 0
while len(listaIndicesAleatorios) < numeroDeInstanciasEntrenamiento:
	num = random.randint(0,numeroDeInstancias-1)
	#print(num, " está en la lista?: ",num in listaIndicesAleatorios)
	if num not in listaIndicesAleatorios:
		listaIndicesAleatorios.append(num)
#print(listaIndicesAleatorios)
ConjuntoEntrenamiento = ConjuntoInicial.iloc[listaIndicesAleatorios]

listaIndicesPrueba = []
for h in range(numeroDeInstancias):
	listaIndicesPrueba.append(h)

#print(listaIndicesPrueba)
for i in listaIndicesAleatorios:
	if i in listaIndicesPrueba:
		listaIndicesPrueba.remove(i)

#print(listaIndicesPrueba)

ConjuntoPrueba = ConjuntoInicial.iloc[listaIndicesPrueba]
 
print("Se han encontrado ", numeroDeInstancias, " instancias en el Conjunto Inicial")
print("El porcentaje de instancias de entrenamiento es:\t", porcentajeEntrenamiento, "%")
print("El porcentaje de instancias de prueba es:       \t", 100-porcentajeEntrenamiento, "%")
print("En consecuencia se determina que")
print("Se usarán ", numeroDeInstanciasEntrenamiento," instancias para aentrenamiento y")
print("se usarán ", numeroDeInstancias - numeroDeInstanciasEntrenamiento," instancias para prueba.")
print("\n")

print("Conjunto de Datos de Entrenamiento:")
print(ConjuntoEntrenamiento)
print("\n")
print("Conjunto de Datos de Prueba:")
print(ConjuntoPrueba)
print("\n")

###########################

listaAtributos = ConjuntoInicial.columns.tolist()
listaAtributos.remove(nombreClase)
listaClases = ConjuntoInicial[nombreClase].unique().tolist()
print(listaAtributos)
print(listaClases)
print("\n")

TablaDatatypes = ConjuntoInicial.select_dtypes(exclude=['int64', 'bool'])
listaAtributosCategoricos = TablaDatatypes.columns.tolist()
listaAtributosCategoricos.remove(nombreClase)
print(listaAtributosCategoricos)

for atributo in listaAtributosCategoricos:
	print(ConjuntoInicial[atributo].unique().tolist())
	print(ConjuntoInicial[[atributo,nombreClase]])
	dframe = pandas.DataFrame(columns=["Valor"]+listaClases)
	dframe = dframe.astype('int64')
	dframe["Valor"] = dframe["Valor"].astype("object")
	auxList = []
	k=0
	for valor in ConjuntoInicial[atributo].unique().tolist():
	# 	auxList.append({"Valor": valor, })
		auxDicc = {"Valor": valor}
		for clase in listaClases:
			auxDicc[clase] = len(ConjuntoInicial[(ConjuntoInicial[atributo].str.contains(str(valor)) & ConjuntoInicial[nombreClase].str.contains(str(clase)))].index)
		print(auxDicc)
		dframe[k] = auxDicc
		k+=1	
	print(dframe)	

	print('prueba')
	 


#print(TablaDatatypes)

# print(ConjuntoInicial[(ConjuntoInicial[atributo])])


