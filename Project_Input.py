import Project_Convert
import Project_Layout

def Number_Check(num):
    check=0
    Number_length=len(num)
    if Number_length==8:
        count=7
        num_check=0
        while count>=0:
            if int(num[count])==0 or int(num[count])==1:
                num_check=num_check+1
            count=count-1
        if num_check==8: check=1
        return num,check
    elif Number_length>0 and Number_length<=3:
        if int(num)>=0 and int(num)<=255:
            check=1
            num_new=Project_Convert.Conversion(int(num))
            return num_new,check
    else:
        pass

def Number_Input():
    Project_Layout.Message_Header()
    while True:
        try:
            num1=input("Enter a number: ")
            n1,check=Number_Check(num1)
            if check==1: break
        except Exception:
            Project_Layout.Error_Input()
        else:
            Project_Layout.Error_Input()
            
    while True:
        try:
            num2=input("Enter second number: ")
            n2,check=Number_Check(num2)
            if check==1: break
        except Exception:
            Project_Layout.Error_Input()
        else:
            Project_Layout.Error_Input()
            
    return n1,n2
