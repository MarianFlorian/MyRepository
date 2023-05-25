#min si max din lista
def mm():
    n = int(input())
    min = 9999
    max = 0
    lista = []
    for i in range(0,n):
        lista.append(int(input()))
        if lista[i] > max:
            max = lista[i]
        if lista[i] < min:
            min = lista[i]
    print(min,max)

#metoda 2
def min_max(lista):
    min = [0]
    max = [0]
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]
        if lista[i] < min:
            min = lista[i]
    min1 = [0]
    max1 = [0]
    for i in range(len(lista)):
        if lista[i] > max1 and lista[i]!=max:
            max1 = lista[i]
        if lista[i] < min and lista[i] != min:
            min1 = lista[i]
    print(min, max)

def min_max2(lista):
    lista = sorted(lista)
    min = lista[0]
    min1 = lista[1]
    max = lista[len(lista)-2]
    max1 = lista[len(lista)-1]
    print(min,min1,max,max1)

def parcurgere_m(matrice):
    n = len(matrice)
    sir = "abcd" #sir de aceeasi dimensiune cu n
    for i in range(n):
        for j in range(n):
            if matrice[i][j] == 1 and i!=j:
                print(sir[i],sir[j], end="/")

def rec(n):
    s = 0
    if n == 0:
        return 1
    for i in n:
        if i == 0:
            s+=1
    return s

def nr_zero(n):
    if n == 0:
        return 0
    if n % 10 == 0:
        return 1 + nr_zero(n//10)
    else:
        return nr_zero(n//10)
if __name__ == "__main__":
    #parcurgere_m([[1,1,1],[1,1,1],[1,1,1]])
    #min_max2([3,25,2,45,1,14])
    print(nr_zero(10001))