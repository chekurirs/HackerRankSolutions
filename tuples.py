if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    
   # print(integer_list)
    hash_value =hash(integer_list)
    print(hash_value)
