# Cognizant-digital-nuture

## EX:01:Simple Hello World 
## code:
```
print("Hello World!")
```
## output:
<img width="1613" height="216" alt="Screenshot 2026-05-29 095920" src="https://github.com/user-attachments/assets/a57501d2-631e-4e79-9de8-6131dfd87e43" />



## EX:02:Jupyter Notebook 
## code:
```
print("Ny First Notebook")

```
## output:
<img width="1500" height="365" alt="Screenshot 2026-05-29 101756" src="https://github.com/user-attachments/assets/a061902c-d39a-427a-b656-9e8d1c0da25c" />


## EX:03:VS Code Setup 
## code:
```
print("Hello World")
```
## output:

<img width="1613" height="163" alt="image" src="https://github.com/user-attachments/assets/2b59086a-1eaf-4b8b-a428-9f6b038bf316" />

## EX:04:Float Precision 
## code:
```
def net_salary(salary, tax_rate):
    if salary < 0:
        print("Invalid salary")
        return 
    
    if tax_rate < 0 or tax_rate > 1:
        print("Invalid tax rate (must be between 0 and 1)")
        return

    total_salary = salary - (tax_rate * salary)
    
    print(f"The net salary is {total_salary:.2f} rupees")

salary = float(input("Enter the salary: "))
tax = float(input("Enter the tax rate: ")) 
net_salary(salary, tax)


```
## output:
<img width="1455" height="111" alt="image" src="https://github.com/user-attachments/assets/fd5893c4-53df-4d5f-9868-24e1e11b96f0" />


## EX:05:Multiple Assignment
## code:
```
def coord(coordinates):
    if len(coordinates) != 2: 
        print("Invalid coord")
        return
    
    x, y = coordinates
    print(f"The coordinates are: X={x:.2f}, Y={y:.2f}")

pt1 = float(input("Enter the first coordinate: "))
pt2 = float(input("Enter the second coordinate: "))

coord([pt1, pt2])

```
## output:
<img width="504" height="202" alt="image" src="https://github.com/user-attachments/assets/5c096feb-79ee-41d5-8b25-219118561ea8" />


## EX:06:Modulo Operator 
## code:
```
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
## output:
<img width="1465" height="161" alt="image" src="https://github.com/user-attachments/assets/ee91fea3-bc5a-4b34-b29e-f2758c1246de" />


## EX:07:Floor Division
## code:
```
def floordivision(bill,people):
    share=bill//people
    print("Total Bill: ",bill)
    print("Number of peoples: ",people)
    print("Individual Share: ",share)

bill=int(input("Enter the amount"))
people=int(input("Enter the number of peoples:"))
floordivision(bill,people)


```
## output: 
<img width="1438" height="154" alt="image" src="https://github.com/user-attachments/assets/0de61fc1-f58a-46eb-909a-13dc37ce4ee7" />


## EX:08: MIN MAX
## code:
```
def minmax(salary):
    minimum=min(salary)
    maximum=max(salary)
    print("Minimum Salary in the given list is ",minimum)
    print("Maximum Salary in the given list is ",maximum)

salary = list(map(int, input("Enter the salary: ").split()))
minmax(salary)

```
## output:
<img width="1449" height="111" alt="image" src="https://github.com/user-attachments/assets/e87a9117-eced-43af-951b-d908756ef64d" />


## EX:09: User Input
## code:
```
def user(name):
    print(name ,", Have a great day")

name=input("Enter your name:")
user(name)
```
## output:
<img width="1447" height="89" alt="image" src="https://github.com/user-attachments/assets/8aaca5ed-865e-4e84-9b2d-eeb494d8c631" />



## EX:10 : Numeric Input
## code:
```
def numeric():
    age=int(input("Enter you age: "))
    print("Next year you'll be ",age+1)

numeric()
```
## output:
<img width="1452" height="86" alt="image" src="https://github.com/user-attachments/assets/44f74a97-b28e-489f-987d-ca75a6d4943d" />


## EX:11 : Float Input
## code:
```
def weight():
    wt=float(input("Enter the weight in kg: "))
    lbs=wt*2.20462
    print("The given weight in kg is: ",wt)
    print("The weight after converting from kg to pounds is: ",lbs)

weight()
```
## output:
<img width="1461" height="120" alt="image" src="https://github.com/user-attachments/assets/3669e354-7fc8-4f12-892b-36eaf2862c35" />


## EX:12 : Simple if

## code:
```
def num():
    x=int(input("Enter a number:"))
    if(x%2==0):
        print("The given number is even")
    else:
        print("The given number is odd")

num()
```
## output:
<img width="1452" height="98" alt="image" src="https://github.com/user-attachments/assets/00ea80e9-8560-46f4-8f7f-a04278d163a5" />


## EX:13 : If-else
## code:
```
def condition(marks):
    if(marks<50):
        print("Fail")
    else:
        print("Pass")

marks=int(input("Enter the mark obtained: "))
condition(marks)
```
## output:
<img width="1445" height="86" alt="image" src="https://github.com/user-attachments/assets/12d91135-32c7-439f-8eb1-2a0c312de8e9" />

## EX:14 : If-Elif-Else
## code:
```
def grade():
    marks=int(input("Enter the mark obtained"))
    if(marks>90):
        print("The grade obtained is A")
    elif(marks >80 and marks <65):
        print("The grade obtained is B")
    else:
        print("The grade obtained is C")

grade()
```
## output:
<img width="1446" height="91" alt="image" src="https://github.com/user-attachments/assets/58a8279c-c462-4dd1-ad2d-b750a71c26ad" />

## EX:15 : Nested If
## code:
```
def login(user, pwd):
    if user.strip() == "" or pwd.strip() == "":
        print("Username or Password cannot be blank")
    else:
        if user == "admin":
            if pwd == "pass123":
                print("Login Successful")
            else:
                print("Invalid Password")
        else:
            print("Invalid Username")

user = input("Enter username: ")
pwd = input("Enter password: ")
login(user, pwd)

```
## output:
<img width="1461" height="151" alt="image" src="https://github.com/user-attachments/assets/ae90c7cd-32f3-46c2-9e8d-4a0f6a6acd51" />


## EX:16 : For Loop
## code:
```
def forloop():
    num=int(input("Enter a number: "))
    for i in range(1,num+1):
        print(i,end=" ")

forloop()
```
## output:
<img width="1458" height="91" alt="image" src="https://github.com/user-attachments/assets/871b44d0-952a-4a22-8cee-4fd6a94f9ab4" />


## EX:17 : While Loop
## code:
```
def iter():
    num=int(input("Enter a number: "))
    while (num>0):
        print(num)
        num-=1
iter()
```
## output:
<img width="1447" height="178" alt="image" src="https://github.com/user-attachments/assets/713bc141-6316-4098-b494-eeddcf617b55" />


## EX:18 : Break
## code:
```
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

```
## output:
<img width="1447" height="114" alt="image" src="https://github.com/user-attachments/assets/0101d995-e419-42b0-b66b-d90f29059ec1" />

## EX 19 : Continue

## code:
```
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
```
## output:
<img width="1440" height="118" alt="image" src="https://github.com/user-attachments/assets/1fc3073b-55a1-45cd-9613-0e83fbb12e52" />

## EX 20 : Pass

## code:
```
def empty_function():
    pass

empty_function()
print("Function defined")
```
## output:
<img width="1450" height="93" alt="image" src="https://github.com/user-attachments/assets/b10b472b-0db3-4461-b5c9-558a5d980e7c" />

## EX 21 : Consistent Indentation

## code:
```
def check_nested():
    if True:
        if True:
            print("Nested")

check_nested()
print("Confirmation message")
```
## output:
<img width="1456" height="98" alt="image" src="https://github.com/user-attachments/assets/9ab57df8-f8f9-4c07-9cff-54ec2a95baf3" />

## EX 22 : Comment Usage

## code:
```
def calculate_salary():
    base_salary = int(input("Enter base salary: "))
    bonus = int(input("Enter bonus: "))
    total_salary = base_salary + bonus
    print("Total Salary:", total_salary)

calculate_salary()
```
## output:
<img width="1461" height="149" alt="image" src="https://github.com/user-attachments/assets/17ce1751-03c5-4d1a-ba87-ee1a7180c5c4" />



