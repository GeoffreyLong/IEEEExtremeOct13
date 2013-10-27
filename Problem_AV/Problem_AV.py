import sys

def recur(curX, curY, endX, endY, oasis, wDays, totDays):
    if(wDays<=5):
        if(curX == endX and curY == endY):
            return totDays
        else:
            
            return(recur(0, 0, endX, endY, oasis, wDays+1, totDays+1))
    else: 
        return 10000000

alist = []
for line in sys.stdin:
    alist.append(line.rstrip('\n'));
    
yDim = int(alist[0].split(" ")[0])
xDim = int(alist[0].split(" ")[1])+1

alist.reverse()
alist.pop()
alist.reverse()
oasis = []
start = []
end = []
matrix = [[0]*(xDim) for i in range(yDim)]
i = 0
j = 0
for l in alist:
    j=0
    for ln in list(l):
        matrix[i][j] = ln
        if (ln=="+"):
            oasis.append(str(i)+" "+str(j))
        if (ln=="S"):
            start.append(str(i)+" "+str(j))
        if (ln=="E"): 
            end.append(str(i)+" "+str(j))
        j+=1
    i+=1
    

#recur(start[0].split(" ")[0], start[0].split(" ")[1], end[0].split(" ")[0], end[0].split(" ")[1], oasis, 0, 0)    

    
    
'''
i = 0
j = 0
for i in range(yDim):
    print(end='\n')
    for j in range(xDim):
        print(matrix[i][j], end='')
'''