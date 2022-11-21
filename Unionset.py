# Enter your code here. Read input from STDIN. Print output to STDOUT

def findatleastone(arr1,arr2):
    
    unionset=arr1.union(arr2)
    
    n1=len(arr1)
    n2=len(arr2)
    
    n3=len(unionset)
    
    total=n1+n2-n3
    print(n3)





if __name__ == '__main__':
    n1 = int(input())
    arr1 = set(map(int, input().split()))
    n2 = int(input())
    arr2 = set(map(int, input().split()))
    findatleastone(arr1,arr2)
    
    #result = average(arr)
   # print(result)
   
   
