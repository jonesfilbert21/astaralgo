g = {
    'Arad': [('Timisoara',118),('Sibiu',140),('Zerind',75)],
    'Bucharest':[('Pitesti',101),('Giurgiu',90),('Fagaras',211),('Urziceni',85)],
    'Craiova':[('Rimnicu Vilcea',146),('Pitesti',97),('Dobreta',120)],
    'Dobreta':[('Mehadia',75),('Craiova',120)],
    'Eforie':[('Hirsova',86)],
    'Fagaras':[('Sibiu',99),('Bucharest',211)],
    'Giurgiu':[('Bucharest',90)],
    'Hirsova':[('Urziceni',98),('Eforie',86)],
    'Iasi':[('Vaslui',92),('Neamt',87)],
    'Lugoj':[('Mehadia',70),('Timisoara',111)],
    'Mehadia':[('Lugoj',70),('Dobreta',75)],
    'Neamt':[('Iasi',87)],
    'Oradea':[('Zerind',71),('Sibiu',151)],
    'Pitesti':[('Bucharest',101),('Craiova',138),('Rimnicu Vilcea',97)],
    'Rimnicu Vilcea': [('Sibiu',80),('Craiova',146),('Pitesti',97)],
    'Sibiu':[('Arad',140),('Oradea',151),('Fagaras',99),('Rimnicu Vilcea',80)],
    'Timisoara':[('Arad',118),('Lugoj',111)],
    'Urziceni':[('Hirsova',98),('Vaslui',142),('Bucharest',85)],
    'Vaslui':[('Iasi',92),('Urziceni',142)],
    'Zerind':[('Arad',75),('Oradea',71)]
}

h ={
    'Arad': 366,
    'Bucharest':0,
    'Craiova':160,
    'Dobreta':242,
    'Eforie':161,
    'Fagaras':178,
    'Giurgiu':77,
    'Hirsova':151,
    'Iasi':226,
    'Lugoj':244,
    'Mehadia':241,
    'Neamt':234,
    'Oradea':380,
    'Pitesti':98,
    'Rimnicu Vilcea': 193,
    'Sibiu':253,
    'Timisoara':329,
    'Urziceni':80,
    'Vaslui':199,
    'Zerind':374
}

def findmatch(mainobj, thingtofind):
    for s in mainobj:
        if s == thingtofind:
            return True       
    return False

def astaralgorithm(thestart,thestop): 
    cur = thestart 
    respath =[] 
    curpath = []
    curpath.append([[cur,],0])
  
    while True:       

        if len(curpath) == 0:
            respath.append(["Path Not Found!",])
            break

        y = 1
        theoptimal = curpath[0]
        curindex =0
        while y<len(curpath):
            hx1 = h.get(curpath[curindex][0][-1])
            hx2 = h.get(curpath[y][0][-1])
            if (curpath[curindex][1] + hx1) > (curpath[y][1] + hx2) :
                curindex = y
                theoptimal.clear
                theoptimal = curpath[y]
            y+=1
      
        if theoptimal[0][-1]== thestop:
            respath.append(theoptimal[0])
            respath.append(theoptimal[1])
            break
        else:
            for plusassign in g.get(theoptimal[0][-1]):
                if findmatch(theoptimal[0], plusassign[0]) == True:
                    continue
                else:
                    t = theoptimal[1] + plusassign[1]
                    curpath.append([theoptimal[0]+[plusassign[0],],t])
            curpath.pop(curindex)
    finalgx = respath[1]
    finalhx = h.get(respath[0][-1])
    finalfx =finalgx+finalhx
    thefinalpath = str(respath[0])
    thefinalpath = thefinalpath.translate({ord('['):None})
    thefinalpath = thefinalpath.translate({ord(']'):None})
    thefinalpath = thefinalpath.translate({ord("'"):None})
    thefinalpath = thefinalpath.replace(',','->')
    print(thefinalpath)
    print(finalfx , " = " , finalgx , " + " , finalhx)

while True:
    startplace = input('Type the start city:')
    stopplace = input('Type the stop city:')
    astaralgorithm(startplace,stopplace)
    thecont = input('Do you want to check more?(y/else): ')
    if thecont.lower() == 'y':
        continue
    else:
        print('Thank You!')
        break