# Enter your code here. Read input from STDIN. Print output to STDOUT


# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    
    n1 = int(input())
    
    for i in range(n1):
        
        setAsize=int(input())
        arrA = set(map(int, input().split()))
        
        setBsize=int(input())
        arrB=set(map(int,input().split()))
        
        intersect=arrA.intersection(arrB)
        
        if intersect==arrA:
            print(True)
        else:
            print(False)

