def Addition(n1,n2):
    #half adder
    ext1=eval(n1[7])
    ext2=eval(n2[7])
    temp_and=ext1&ext2
    temp_xor=ext1^ext2
    result=str(temp_xor)

    #full adder
    count=6
    temp=temp_and
    while count>=0:
        
        ext1=eval(n1[count])
        ext2=eval(n2[count])
        temp_and=ext1&ext2
        temp_xor=ext1^ext2

        temp_and2=temp_xor&temp
        temp_xor2=temp_xor^temp
        temp=temp_and|temp_and2
        result=str(temp_xor2)+result
        count=count-1
    return result, temp
