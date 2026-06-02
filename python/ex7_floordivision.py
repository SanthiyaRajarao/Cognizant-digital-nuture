def floordivision(bill,people):
    share=bill//people
    print("Total Bill: ",bill)
    print("Number of peoples: ",people)
    print("Individual Share: ",share)

bill=int(input("Enter the amount"))
people=int(input("Enter the number of peoples:"))
floordivision(bill,people)

