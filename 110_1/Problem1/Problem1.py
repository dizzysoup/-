def search(data,left,right,key): 
    mid = (left+right)//2  
    if data[mid] == key:
        return mid 
    if left == right :
        return -1 
    if data[mid] > key:
        return search(data,left,mid,key)    
    else:
        # errorcode 
        # return search(data,mid,right,key)
        return search(data,mid+1,right,key)
def f(x):
    print(search([1,5,9,14,23,26],0,5,x))
    # 1-5
    data = [1,5,9,14,23,26]
    my_dict = {}
    my_dict[9] = search(data,0,5,9)
    my_dict[1] = search(data,0,5,1)
    my_dict[14] = search(data,0,5,14)
    print(my_dict)
    print(data[1:5:2])


def main():
    f(26)

if __name__ == '__main__':
    main()