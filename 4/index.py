
def main():
    print "Starting challenge 4:\n"
    arr = getArr()
    num = getPosInt(arr)
    print num

def getArr():
    return [1,2,0]

def getPosInt(arr):
    inUse = {}
    for i in arr:
        if i > 0: 
            inUse[i] = True
    return find(inUse, 1)

def find(inUse, num):
    if(num not in inUse):
        return num
    return find(inUse, num+1)

if __name__ == "__main__":
    main()
