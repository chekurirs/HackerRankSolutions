def average(array):
    setmarks=set(array)
   # setmarks.update(array)
    sumvalue=0
    for i in setmarks:
        sumvalue=sumvalue+i
        
    #print(sumvalue/len(setmarks))
    return sumvalue/len(setmarks)
      
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
