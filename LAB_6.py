#def cautare(lista, element):
 #   for i in range(len(lista)):
  #      print(lista[i])
  #      if lista[i] == element:
   #         return i
    #    return -1
# print(cautare((24,3,20,5,12), 5))
#def selectionSort(itemsList):
 #   n = len(itemsList)
  #  for i in range(n):
   #     minValueIndex = i
    #    for j in range(i+1,n):
     #       if itemsList[j] < itemsList[minValueIndex]:
      #          minValueIndex = j
#
 #       if minValueIndex !=i:
  #          temp = itemsList[i]
   #         itemsList[i] = itemsList[minValueIndex]
    #return itemsList

#data = [9,5,1,4,3]
#selectionSort(data)
#print(data)

employee1 = {
    'id': 14,
    'name': 'Jhon Doe',
    'age': 34,
    'position':'Business Manager'
}
employee2 = {
    'id': 2,
    'name': 'Jhon',
    'age': 28,
    'position': 'N/A'
}
employee3 = {
    'id': 110,
    'name': 'Jhon Smith',
    'age': 40,
    'position': 'Software Developer'
}
employee4 = {
    'id': 40,
    'name': 'Jhon Smith',
    'age': 35,
    'position': 'Engineer'
}
list1 = [employee1, employee2,employee3,employee4]
def cautareID(lista,id_cautat):
    for i in range(len(lista)):
        if lista[i]['id'] == id_cautat:
            return lista[i]
        return None
print(cautareID(list1,2))


#def pozitie(angajat):
 #   return angajat['position']
#print(pozitie(employy))

