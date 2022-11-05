def Sort(List):
    List.sort(key = lambda l: l[0])
    return List

if __name__ == '__main__':
    
    inputlist=[]
    
    Fminima=10000000.0000000000
    Sminima=10000000.0000000000
    
    Sminimalist=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        if score < Fminima:
            Sminima=Fminima
            Fminima=score
            
        elif (score<Sminima)and(score!=Fminima):
            Sminima=score
            
        a=[name,score]
            
        inputlist.append(a)
        
    #print(Sminima)
    rsltnameslst=[x for x in inputlist if str(Sminima)== str(x[1])]
    sortedlst=Sort(rsltnameslst)
    #print(rsltnameslst)
    
    
    for x in rsltnameslst:
        print(x[0])
    
    #print(rsltnameslst)
    
   # print(inputlist)
    #print(Fminima)
    #print(Sminima)