
#ASSIGNMENT 1




#Question 1

# to find avgerage of three numbers



print("ASSIGNMENT 1")
print()

print("Question 1")
print("to find avgerage of three numbers")
print()


a = int(input("Enter first number : ")) #taking first input
b = int(input("Enter second number : ")) #taking second input
c = int(input("Enter third number : ")) #taking third input

avg_num = (a+b+c)/3
#formula for average

print("average of numbers is ",avg_num)

#Question 2

#to find the tax payable
print()
print("Question 1")
print("to find the tax payable")
print()

gross_income = int(input("Enter your Gross Income in nearest integer :   "))
dependent =  int(input("Enter total number of dependents  :"))

dep_deduct =  dependent*3000
tax_rate=0.2
taxable_income = gross_income - dep_deduct - 10000

if taxable_income > 0:
    tax = taxable_income*tax_rate
    print("Total payable tax =  ",tax)
else:
    print("you dont have to pay a single penny of tax")


#Question 3

# to store the student data into list

print()
print("to store the student data into list")
print(" Question - 3 ")

_sid = int(input("Enter your sid :  "))
name = input("Enter your name : ")
gender =  input(" Enter your gender ( F , M , U)  :")
Course_name = input("Enter your course name : ")
CGPA = float(input("Enter your CGPA : "))

data = [_sid,name,gender,Course_name,CGPA]

print(data)


#Question 4

# to store the students marks  in a list in a sorted  order

print()
print("Question 4")
print("to store the students marks  in a list in a sorted  order")

a = int(input("Enter first marks : "))
b= int(input("Enter your second marks : "))
c= int(input("Enter your third marks : "))
d= int(input("Enter your fourth marks : "))
e= int(input("Enter your fifth marks : "))

marks=[a,b,c,d,e] #list of marks

marks.sort()
print(marks)


# Question 5

print()
print("Question 5 :  ")
print("Question related to list of colours")
print()


colours=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("given list ", colours)

# First Task

colours.pop(3)
print(" 1st task to remove 4th element ")
print(colours)


# Second Task
colours=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("2nd task  to  remove  Black and Pink  and change it to purple :  ")

#in one line
colours[3:4] = ["purple"]

print(colours)
