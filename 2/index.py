#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?
from functools import reduce


def main():
    print "Starting challenge 2 \n"
    array = getArray()
    print "the given array is:"
    print array
    opt1 = withDevision(array)
    opt2 = noDevision(array)
    print "\nfirst with devision:"
    print opt1
    print "\nsecond devision:"
    print opt2

def getArray():
    return [1, 2, 3, 4, 5]

def withDevision(array):
    product = reduce(lambda a,b : a*b, array)
    return map(lambda i: product/i, array)

def noDevision(array):
    newArr = array[:]
    for x in range(0,len(array)):
        product = 1
        for y in range(0,len(array)):
            if(y != x):
                product = product * array[y]
        newArr[x] = product
    return newArr

if __name__ == "__main__":
    main()
