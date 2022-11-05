if __name__ == '__main__':
    N = int(input())
    list=[]
    
    for i in range(0,N):
        
        inputstr=str(input())
        
        if "insert" in inputstr:
            
            s = [int(s) for s in str.split(inputstr) if s.isdigit()]
            list.insert(s[0],s[1])
        
        elif "remove" in inputstr:
            s = [int(s) for s in str.split(inputstr) if s.isdigit()]
            list.remove(s[0])
        
        elif "append" in inputstr:
            s = [int(s) for s in str.split(inputstr) if s.isdigit()]
            list.append(s[0])
        
        elif "sort" in inputstr:
            list.sort()
        
        elif "pop" in inputstr:
            list.pop()
            
        elif "reverse" in inputstr:
            list.reverse()
            
        elif "print" in inputstr:
            print(list)