# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    
    n1 = int(input())
    arr1 = list(map(int, input().split()))
    #arr2=set(arr1)
    
    #unique=[i for i in arr2 if arr1.count(i)==1]
 
    
    #print(unique[0])
    
    found = set()
    found_again = set()

    for a in arr1:
        if a in found_again:
            continue
        if a in found:
            found.remove(a)
            found_again.add(a)
        else:
            found.add(a)

    [print(i) for i in found]

