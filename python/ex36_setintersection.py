def common_elements():
    set1 = set()
    set2 = set()
    n1 = int(input("Enter number of elements in set1: "))
    for i in range(n1):
        set1.add(int(input("Enter element for set1: ")))
    n2 = int(input("Enter number of elements in set2: "))
    for i in range(n2):
        set2.add(int(input("Enter element for set2: ")))
    common = set1 & set2
    print("Set1:", set1)
    print("Set2:", set2)
    print("Common elements:", common)

common_elements()