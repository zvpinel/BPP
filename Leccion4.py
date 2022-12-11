#Ejercicio 1
import pdb
pdb.set_trace()

print("_______1er ejercicio________\n")
listaEnteros = [[2,4,1], [1,2,3,4,5,6,7,8],[100,250,43]]

for i in range(len(listaEnteros)):
    print("Lista: ", listaEnteros[i])
    print("*** Máximo valor de lista: ", max(listaEnteros[i]))    

'''def mayor_lista(listaEnteros):
    valMax = listaEnteros[0]
    for i in listaEnteros:
        if i > valMax:
            valMax = i
    return valMax

def main(listaEnteros):
    print("El mayor de la lista es: ", mayor_lista(listaEnteros))

main(listaEnteros)'''

#Ejercicio 2
def primos_func(num):
  for i in range(2,num):
    if (num%i) == 0:
      return False
  return True

primos =  [3, 4, 8, 5, 5, 22, 13]

print("\n_______2do ejercicio________")
print(list(filter(primos_func,primos)))
