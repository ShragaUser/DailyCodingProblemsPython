from index import withDevision,noDevision
from time import time

def main():
    ARR = [1,2,3,4,5]
    start = time()
    withDevision(ARR)
    stop = time()
    print (stop - start)
    start = time()
    noDevision(ARR)
    stop = time()
    print (stop - start)

if __name__ == "__main__":
    main()
