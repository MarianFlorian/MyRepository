def rec(n):
    if n == 0:
        return 0
    return n + rec(n-1)

def suma_lista():
    suma_lista = []
    suma = 0
    n = int(input())
    for i in range(n):
        suma_lista.append(int(input()))
    for i in range(suma_lista):
        suma = suma_lista - len(suma_lista) + suma_lista[-1]
    print(suma)

def suma_rec(lista):
    if len(lista) == 1:
        return 0
    else:
        mij = len(lista) // 2
        return suma_rec(lista[:mij] + suma_rec(lista[mij:])

    lst_imp = [4, 1, 5, 3]
    print(suma_rec(lst_imp))

def sololearn():
    nums = list(range(3, 15, 3))

    print(nums[2])
if __name__ == "__main__":
    sololearn()
