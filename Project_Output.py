import Project_Layout
def Project_Display(result,temp):
    if temp==0:
        print("\nSum in binary is:",result)
        print("Sum in decimal is:",int(result,2))
    else:
        Project_Layout.Error_Sum()
