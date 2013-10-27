import sys
alist = []
for line in sys.stdin:
    line = line.strip('\r')
    line = line.strip('\n')
    line = line.strip('\r\n')
    alist.append(line)
    
alist.reverse()
alist.pop()

blist = []
blist = alist[0].split(" ")

toCiph = alist[0]

totList = []
comboList = []
for a in alist:
    for b in blist:
        if (len(a)==len(b)):
            comboList.append(str(a) + " " + str(b))
            totList.append(str(a))
            totList.append(str(b))
                
dct = {}    
    
for cl in comboList:
    if (totList.count(cl.split(" ")[0]) == 1):
        lstA = list(cl.split(" ")[0])
        lstB = list(cl.split(" ")[1])
        lstA.reverse()
        for b in lstB:
            dct[b] = lstA.pop()


for cl in comboList:
    lstA = list(cl.split(" ")[0])
    lstB = list(cl.split(" ")[1])
    for b in lstB:
        if (b in dct):
            print (b)
    
            
finalString = ""
for c in toCiph:
    if (c==" "):
        finalString+=" "
    else:
        finalString+=dct[c]
print(finalString.upper())