def Conversion(num):
    num_bin=bin(num)[2:]
    num_list=list(num_bin)
    num_length=len(num_list)
    num_new_length=8-num_length
    for count in range(0,num_new_length):
        num_list.insert(count,"0")

    return num_list
