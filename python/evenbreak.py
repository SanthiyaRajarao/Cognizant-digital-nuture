def first_even(start, end):
    if start > end:
        print("Invalid range: start should be less than or equal to end")
        return

    for i in range(start, end + 1):
        if i % 2 == 0:
            print("First even number is:", i)
            break
    else:
        print("No even number found in the given range")

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

first_even(start, end)