def grade():
    marks=int(input("Enter the mark obtained"))
    if(marks>90):
        print("The grade obtained is A")
    elif(marks >80 and marks <65):
        print("The grade obtained is B")
    else:
        print("The grade obtained is C")

grade()