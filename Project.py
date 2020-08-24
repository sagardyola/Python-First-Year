import Project_Input
import Project_Add
import Project_Layout
import Project_Output

choice="Y"
while (choice.upper()=="Y"):
    n1,n2=Project_Input.Number_Input()
    result,temp=Project_Add.Addition(n1,n2)
    Project_Output.Project_Display(result,temp)
    
    while True:
        choice=input("Do you want to continue(Y/N)?")
        if choice.upper()=="Y" or choice.upper()=="N":
            print()
            break
        else:
            Project_Layout.Error_Input()
