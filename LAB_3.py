
#matrice patratica, sa se determine max si min
def mat1():
    n = int(input())
    m = int(input())

    matrice = []
    for i in range(n):
        linie = []
        for j in range(m):
            linie.append(int(input()))
        matrice.append(linie)

    max = 0
    min = 9999
    imin = ""
    imin = ""
    for i in range(n):
        for j in range(n):
            if (matrice[i][j] > max):
                max = matrice[i][j]
                imax = i + "," + j
            if(matrice[i][j] < min):
                min = matrice[i][j]
                imin = i +"," +j
    print(min)
    print(max)


#se da o matrice patratica, sa se genereze elementele matricii dupa urmatoarele reguli:
# elementele pt care produsul indiclor este un nr par vor avea valoarea 1
#elem pt care produsul indicilor este un nr impar vor avea val 0
# elem de pe diagonala principala vor avea valoarea 2

def mat2(matrice):
    m = len(matrice)
    n = len(matrice[0])
    for i in range(m):
        for j in range(n):
            if i*j % 2 == 0:
                matrice[i][j] = 1
            if i*j % 2 != 0:
                matrice[i][j] = 0
            if i == j:
                matrice[i][j] = 2

#---------------- DIVIDE et IMPERA
def unire(lista_stanga, lista_dreapta):
    rezultat = []
    i = 0
    j = 0
    while i < len(lista_stanga) and j < len(lista_dreapta):
        if lista_stanga[i] < lista_dreapta[j]:
            rezultat.append(lista_stanga[i])
            i+=1
        else:
            rezultat.append(lista_dreapta[j])
            j+=1
    while i < len(lista_stanga):
        rezultat.append(lista_stanga[i])
        i+=1
    while j < len(lista_dreapta):
        rezultat.append(lista_dreapta[j])
        j+=1

def msort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mij = len(lista) // 2
        stanga = msort(lista[::mij])
        dreapta = msort(lista[mij::])

        return unire(stanga, dreapta)

if __name__ == "__main__":
    mat2(matrice)