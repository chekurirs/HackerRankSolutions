# Enter your code here. Read input from STDIN. Print output to STDOUT
def symmetricdiff(array1,array2):
    
    array1=set(array1)
    array2=set(array2)
    #print(array1)
    #print(array2)
    c=array1.difference(array2)
    d=array2.difference(array1)
    f=c.union(d)
    f=sorted(f)
    [print(i) for i in f]




if __name__ == '__main__':
    n1 = int(input())
    arr1 = list(map(int, input().split()))
    n2 = int(input())
    arr2 = list(map(int, input().split()))
    symmetricdiff(arr1,arr2)
    #result = average(arr)
   # print(result)

