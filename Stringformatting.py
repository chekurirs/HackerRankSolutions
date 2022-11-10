def print_formatted(number):
    
    binaryeq=bin(number)
    bitwidth=len(binaryeq[2:])
    bitwidth+=1
    for i in range(1,number+1):
        inputstring=str(i)
        inputstring=inputstring.rjust(bitwidth-1,' ')
        octstring=oct(i)
        octstring=octstring[2:]
        octstring=octstring.rjust(bitwidth,' ')
        hexstring=hex(i)
        hexstring=hexstring[2:]
        hexstring=hexstring.rjust(bitwidth,' ')
        hexstring=hexstring.upper()
        binarystring=bin(i)
        binarystring=binarystring[2:]
        binarystring=binarystring.rjust(bitwidth,' ')
        
       # print(str(i)+' ' * bitwidth+octstring[2:]+' ' * bitwidth+hexstring[2:]+' ' * bitwidth+binarystring[2:])
        
        print(inputstring+octstring+hexstring+binarystring)
        
    # your code goes here

if __name__ == '__main__':
