def first_even(start, end):
    if start > end:
        print("Invalid range: start should be less than or equal to end")
        return
    sum=0
    for i in range(start, end + 1):
        if i % 2 == 0:
            continue
        sum+=i
    print("The sum of odd numbers in the given range is: ",sum)

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

first_even(start, end)