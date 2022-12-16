'''Buenas Practicas de programación - Lección 1. 
***Ejercicio 1:
- Crea una funcion que pida por pantalla un número al usuario y que controle mediante excepciones:
a. Solo se podrá introducir números enteros
b. Si el numero es mayor de 10 lanza una excepción con raise la cual hayas creado previamente 
mediante ‘class Miexcepcion(Exception):’'''

def Miexcepcion(num):
    if num < 0:
        raise ValueError("Debe ingresar sólo números positivos")
    elif num > 10:
        raise ValueError("Número ingresado debe ser menor a 10")   

def userNumber():
    while True:
        try:
            num = int(input("Introduzca número entero entre 0 y 10: "))
            Miexcepcion(num)
            break

        except Exception as e:
            print("Error de sistema: ", e)
    
    print("Número válido\n")        
        
print("***1. Ejercicio 1***\n")
userNumber()

'''***Ejercicio 2:
Abre un fichero .txt y controla mediante excepciones las diferentes
casuisticas para que el programa no termine de forma inesperada.
Utiliza el finally para cerrar el fichero.
'''
print("***2. Ejercicio 2***\n")

def closetxt(ficheroPath):
    try:
        miFicherotxt.close()
    except:
        print ("Cerrando")

ficheroPath = "fichero.txt"

try:   
    miFicherotxt = open(ficheroPath,"r")
    for i in miFicherotxt:
        print(i)

except FileNotFoundError:
    print("Archivo o directorio inválido")
    
except OSError:
    print("Argumento inválido")

except Exception as e:
    print("Error en fichero: ", e)

finally:
    closetxt(ficheroPath)    

