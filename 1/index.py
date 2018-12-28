#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

#Bonus: Can you do this in one pass?

def main():
    print "Starting coding problem\n"
    array = getArray()
    print "given array: \n"
    print array
    print "\ngiven K \n"
    k = getK()
    print "%d \n"%k
    print "the answer is: \n"
    print addToK(array,k)

def getArray():
    return [10,15,3,7]

def getK():
    return 3

def addToK(array,k):
    tempMap = {}
    for i in array:
        if(i in tempMap):
            return True
        else:
            tempMap[k-i] = True
    return False

if __name__ == "__main__":
    main()
