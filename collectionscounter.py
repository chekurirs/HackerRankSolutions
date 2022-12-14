# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

shosizelistLength = int(input())

sizelist= list(map(int, input().split()))

noofcustomers=int(input())

sizekeys=list(Counter(sizelist).keys())

sizenumbers=list(Counter(sizelist).values())

earnamount=0

#print(sizekeys)
#print(sizenumbers)

for i in range(noofcustomers):
    descrlist=list(map(int,input().split()))
    #print(descrlist)
    
    if descrlist[0] in sizekeys: 
        idx=sizekeys.index(descrlist[0])
    else:
        continue
    
    if sizenumbers[idx]==0:
        earnamount+=0
    else:
        earnamount+=descrlist[1]*1
        sizenumbers[idx]-=1
        
    #print(earnamount)
        
print(earnamount)
    
    
    
    
    
    
    

