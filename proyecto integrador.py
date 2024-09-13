"""
Autor: Frado García Palacios
Matrícula: A01352112

"""
#Librerías---------------------------------------------------------------------------------------------------------------------------------
import random
import time
import glob
import pandas
#------------------------------------------------------------------------------------------------------------------------------------------

#Función que modifica caractéres por los correctos
def caract_correct(x):
    x = x.strip()
    x = x.replace("\n", "")
    x = x.replace("Â¿", "¿")
    x = x.replace("Ã©", "é")
    x = x.replace("Ã¡", "á")
    x = x.replace("Ã±", "ñ")
    x = x.replace("Ã‘", "Ñ")
    x = x.replace("Ã­", "í")
    x = x.replace("Ã³", "ó")
    x = x.replace("Ãº", "ú")
    x = x.replace("Ã¼", "ü")
    x = x.replace("Â¡", "¡")
    return(x)

#Opción a del menú-------------------------------------------------------------------------------------------------------------------------
def diagnostico():
    letra = input("Escoge el grado de secundaria tecleando la letra de la opción deseada:\na) Primer año\nb) Segundo año\nc) Tercer año\n_")
    letra = letra.lower()
    letra = letra.strip()
    
    if letra == "a":
        revolvedor("mate_1.txt")
    elif letra == "b":
        revolvedor("mate_2.txt")
    elif letra == "c":
        revolvedor("mate_3.txt")
    else:
        print("Opción no válida")
        time.sleep(2)
        menu()

#Opción b del menú-------------------------------------------------------------------------------------------------------------------------
def lect_cuest(archivo):           #Lee el archivo y lo converte a una matriz
    matriz_QA = [[], []]                              
    cant_opci = []
    cantidad = 0
    if (len(glob.glob(archivo)) >= 1):  #Comprueba la existencia del archivo
        preguntas = open(archivo, "r")
        while True:
            linea = preguntas.readline()
            if len(linea)==0:
                break
            linea = caract_correct(linea)
            
            if linea.startswith("-"):
                cant_opci.append(cantidad)
                cantidad = 0
                linea = linea.replace("-", "")
                matriz_QA[0].append(linea)
            else:
                cantidad += 1
                matriz_QA[1].append(linea.lower())
        cant_opci.append(cantidad)
        
    else:
        print("Archivo no encontrado")
        menu()
        
    cant_opci.pop(0)
    for opci in cant_opci:
        if opci != cant_opci[0]:
            print("Tu cuestionario no contiene la misma cantidad de opciones para cada pregunta.")
            time.sleep(3)
            menu()
        else:
            None
    preguntas.close()
    return(matriz_QA)   #Regresa una matriz con una columna de preguntas y otra de respuestas

def revolvedor(archi):     #Revuelve las preguntas y las despliega
    matriz = lect_cuest(archi)
    list_rand = []
    aciertos = 0
    cabeza = ["Listado de respuestas"]
    lista_respuestas = matriz[1]
    respuestas_tibble = pandas.DataFrame(data = lista_respuestas, columns = cabeza)  #Dataframe con las respuestas para el caso de que el cuestionario solo tenga una opción por pregunta
    cant_preguntas = len(matriz[0])
    cant_respuestas = len(matriz[1])
    cantidad_opciones = int(cant_respuestas / cant_preguntas)
    incisos = []
    for numero in range (1, cantidad_opciones + 1, 1):
        incisos.append(numero)
        
    if (cant_respuestas == cant_preguntas):
        opcion = str(input("Teclea la letra de la opción deseada:\n\na) Desplegar lista con respuestas.\nb) No desplegar.\n_"))
        opcion = opcion.lower()
        opcion = opcion.strip()
        if opcion == "a":
            print(f"\n{respuestas_tibble}")
        else:
            None
    
    
        while (len(list_rand) < cant_preguntas):
            num = random.randint(0, (cant_preguntas-1))
            if num not in list_rand:
                list_rand.append(num)
                    
        for i in list_rand:
            preg = input(f"\n{matriz[0][i]}\n:")
            preg = preg.lower()
            preg = preg.strip()
            if (preg == matriz[1][i].replace("=", "")):
                aciertos += 1
                print("Correcto")
            else:
                print("Incorrecto")
        print(f"\nObtuviste {aciertos} aciertos de {cant_preguntas}")  
        time.sleep(2)
        menu()
        
    elif (cant_respuestas > cant_preguntas):
        
        while (len(list_rand) < cant_preguntas):
            num = random.randint(0, (cant_preguntas-1))
            if num not in list_rand:
                list_rand.append(num)
                
        for t in list_rand:
            print(f"\n{matriz[0][t]}\n\n")
            for u in range (0, cantidad_opciones, 1):
                sumado = t * cantidad_opciones
                opcionn = matriz[1][sumado + u]
                print(f"{incisos[u]}) {opcionn.replace('=', '')}")
            respuesta_usuario = input("Número: ")
            if ((type(respuesta_usuario) == int) and (respuesta_usuario >= 1) and (respuesta_usuario <= cantidad_opciones)):
                if matriz[1][sumado + respuesta_usuario - 1].startswith("="):
                    aciertos += 1
                    print("\n¡Correcto!")
                    time.sleep(1.5)
                else:
                    print("\n¡Incorrecto!")
                    time.sleep(1.5)
            else:
                print("\n¡Incorrecto!\nRespuesta no válida")
        print(f"\nObtuviste {aciertos} aciertos de {cant_preguntas}")  
        time.sleep(2)
        menu()
            
#------------------------------------------------------------------------------------------------------------------------------------------
    
#Menú para el usuario    
def menu():
    print("\n\n|Programa de estudio y regularización|\n\n\n\nTeclea la letra de la opción deseada:\n")
    time.sleep(1)
    opci = input("a) Examen diagnóstico de matemáticas\nb) Cargar una guía de estudio\nc) Salir del programa\n_")
    opci = opci.lower()
    opci = opci.strip()
    
    if opci == "a":
        diagnostico()
        
    elif opci == "b":
        revolvedor(str(input("El archivo debe estar estructurado por pregunta y \nrespuesta separadas por renglón, no coloques ningún renglón vacío.\nEl número de opciones por cada pregunta debe ser igual.\nCada pregunta deberá contener al principio el caracter guion medio '-' sin espacio.\nLa respuesta correcta de cada pregunta deberá contener al principio el caracter igual '=' sin espacio.\nIntroduce el nombre del archivo txt junto con su extensión\nEjemplo: preguntas.txt\n_")))
    
    elif opci == "c":
        exit()
    
    else:
        print("Opción no válida, intenta de nuevo\n\n\n")
        time.sleep(1.5)
        menu()


      
menu()
    
    



