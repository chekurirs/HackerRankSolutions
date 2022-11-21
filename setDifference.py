# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

def findonlyEnglish(arr1,arr2):
    
    intersect=arr1.intersection(arr2)
    
    diff=arr1.difference(intersect)
    
    n1=len(diff)
    #n2=len(arr2)
    
    #n3=len(unionset)
    
    #total=n1+n2-n3
    print(n1)





if __name__ == '__main__':
    
    n1 = int(input())
    arr1 = set(map(int, input().split()))
    n2 = int(input())
    arr2 = set(map(int, input().split()))
    findonlyEnglish(arr1,arr2)
    
    #result = average(arr)
   # print(result)

