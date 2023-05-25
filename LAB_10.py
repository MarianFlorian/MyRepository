graph =  [[0,1], [0,2],
          [1,2], [1,3],
          [2,4], [2,6],
          [4,5],
          [5,7]]
""""
noduriparcurse = []
def parcurgeregraph(graph, start, noduriparcurse= "", flg):
    if start in noduriparcurse:
        flg = True
    if not flg:
        for element in graph:
            if element[0] == start:
                noduriparcurse.append(start)
                parcurgeregraph(graph, element[1], noduriparcurse,flg)
        if noduriparcurse.count(start) == 0:
            noduriparcurse.append(start)
parcurgeregraph(graph, 0, noduriparcurse,flg)
print(noduriparcurse)

"""
