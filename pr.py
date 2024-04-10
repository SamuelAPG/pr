def input_list():
    list1 = []
    while True:
        x = int(input('put a number: '))
        list1.append(x)
        if x != 0:
            pass
        else:
            return list1

def list_size(list1):
    n = 0
    for i in list1:
        n += 1

    return n

def list_organicer(list1):
    size = list_size(list1)
    
    print(size)
    for i in range(int(size)):
        n = i + 1
        while n < size:
            if (list1[i] > list1[n]):
                x = list1[n]
                list1[n] = list1[i]
                list1[i] = x
                print(list1)
            else:
                pass
            n += 1
            
        pass
    
    return list1

def main():
    list1 = input_list()
    list2 = list_organicer(list1)
    pass

if __name__ == "__main__":
    main()