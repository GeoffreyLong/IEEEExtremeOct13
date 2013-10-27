import sys
def recur(cars, i):
    if (not cars or i>=len(cars)):
        return 0
    else:
        newCars = cars.copy()
        carSize = int(len(cars))
        j=0
        boolean = True
        for j in range(int(carSize/2)):
            if(cars[j]!=cars[carSize-j-1]):
                boolean = False
        if(boolean):
            cars.pop(i)
            return recur(newCars,i+1) + recur(cars, 0) + 1
        else:
            cars.pop(i)
            return recur(newCars,i+1) + recur(cars, 0)
        
    
alist = []
for line in sys.stdin:
    alist.append(line.rstrip('\n'));

cars = list(alist[1])
print(recur(cars,0))

'''
int length = string.length();
            char[] chars = string.toCharArray();
            for (int j = 0; j<length/2; j++){
                if (chars[j]!=chars[length-j-1]){
                    j=length/2;
                }
            }'''