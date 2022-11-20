def merge_the_tools(string, k):
    
    n=len(string)
    substrings=[]
    resultsubstrings=[]
    substringcount=int(n/k)
    substringsize=int(n/substringcount)
    #print(n)
    #print(substringcount)
    for i in range(substringcount):
        tmpstring=string[i*(substringsize):(i+1)*(substringsize)]
        resulttempstring=removerepeatedchar(tmpstring)
        resultsubstrings.append(resulttempstring)
        
    [print(i) for i in resultsubstrings]
   # print(resultsubstrings)
        

def removerepeatedchar(string1):
    
    strlist = []
    for i in range(len(string1)):
        strlist.append(string1[i])

    newlist = []
    j = 0
    for i in range(len(strlist)):
        if string1[i] not in newlist:
            newlist.insert(j, string1[i])
            j = j+1

    resultstr = ""
    resultstr = resultstr.join(newlist)

    return resultstr
    
    

    # your code goes here

if __name__ == '__main__':
