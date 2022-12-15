# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

N=int(input())

ordered_dictionary=OrderedDict()

for i in range(N):
    inputread=list(map(str,input().split()))
    length=len(inputread)
    if length==3:
        inputclass=inputread[0]+' '+inputread[1]
    else:
        inputclass=inputread[0]
    #for i in range(length-1):
    #    inputclass+=' '+inputread[i]
        
    #print(inputclass)
        
    if inputclass in ordered_dictionary:
        prevalue=ordered_dictionary[inputclass]
        ordered_dictionary[inputclass]=prevalue+int(inputread[length-1])
    else:
        ordered_dictionary[inputclass]=int(inputread[length-1])

for keys,values in ordered_dictionary.items():
    
    print(keys,end=' ')
    print(values)
    
    
#print(ordered_dictionary)
        

