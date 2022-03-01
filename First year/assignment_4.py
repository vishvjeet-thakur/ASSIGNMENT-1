# 1. Write a recursive python function to solve the problem of tower of
#    Hanoi with three disks.

print("\nQuestion 1. Tower of Hanoi \n")

def tower(n,present,future,midway,count=0):
    if n==2:
        print(f"Shift disc 1 from {present} to {midway}")
        print(f"Shift disc 2 from {present} to {future}")
        print(f"Shift disc 1 from {midway} to {future}")
        count+=3
        return count
        
    else:
        count+=tower(n-1,present,midway,future)
        print(f"Shift disc {n} from {present} to {future}")
        count+=1
        count+=tower(n-1,midway,future,present)
        return count

number_of_discs = int(input("Number of discs : "))
count = tower(number_of_discs,'A','C','B')
print(f"\nMinimum number of shifts required to move the arrangement of {number_of_discs} from 'A' to 'C'  is  {count}")


# 2. Write a python program to print the Pascal’s triangle for n number of
# rows given by the user using both recursive and iterative procedures
# (for/while loop).

print("\n Question 2 . Pascals Triangle \n")

def triangle_row_recursion(spaces,num_list): # By recursion
    n_list = []
    n_list.append(1)
    if len(num_list)>=2:
        for i in range(len(num_list)-1):
            n_list.append(num_list[i]+num_list[i+1])
    if len(num_list)>=1:
        n_list.append(1)
    
    print("{}".format(" ") *spaces,end='')
    for num in n_list:
        print("{}".format(num),end=" ")
    spaces-=1
    print()
    if spaces>=0:
        triangle_row_recursion(spaces,n_list)

def triangle_row_iteration(rows): # By iteration i.e by uisng for loop
    n_list=[]
    for count in range(rows):
       
        t_list=[]
        print(" "*(rows-1-count),end="")
        if count>1:
            print("1",end=" ")
            t_list.append(1)
            for ch in range(len(n_list)-1):
                print(n_list[ch]+n_list[ch+1],end=" ")
                t_list.append(n_list[ch]+n_list[ch+1])
            t_list.append(1)
            print("1")
            n_list = t_list
        elif count==0:
            print(1)
            n_list.append(1)
        elif count==1:
            print("1 1")
            n_list.append(1)
            
rows = int(input("Enter number of rows: "))
num_list =[]
print("BY recursion :")
triangle_row_recursion(rows-1,num_list)
print("By iteration :")
triangle_row_iteration(rows)


# 3. Input two integer values from user, calculate and print the quotient
#  and reminder obtained from the two values,

print("\nQuestion 3. Use of some inbuilt function -> callable, hash ,set methods etc.\n")
a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))

# as we have to use ony built in functions only..
# using  a inbuilt function  divmod()  to find quotient and remainder 
# divmod() -> it accepts two number and returns tuple containing quotient and remainder


quotient , remainder = divmod(a,b)

print(f"Quotient obtained is  : {quotient}\nRemainder obtained is : {remainder}")

print("\na. Check whether function/values is callable or not .\n")

if callable(divmod):
    print("Function used is callable")
else:
    print("Function used is not callable ")

if callable(a):
    print(f"Value {a} used is callable")
else:
    print(f"Value {a} is not callable ")

if callable(b):
    print(f"Value {b} used is callable")
else:
    print(f"Value {b} is not callable ")

print("\nb. Check whether all the values are non zeroes or not .\n")

values = [quotient,remainder,a,b]
if 0 not in values:
    print("None of the given values and the quotient and remainder obtaineed is zero .")
else:
    if a==0 :
        print("First value of the given input is zero.")
    if b==0:
        print("Second value of the given input is zero.")
    if quotient==0:
        print("Quotient obtained is zero.")
    if remainder==0:
        print("Remainder obtained is zero.")

print("\nc. Add values (4, 5, 6) to the result and filter out the values which are greater than 4.\n")
values.extend([4,5,6])
filtered_values = sorted(list( x for x in values if x>4 ))

print("The filtered values which are greater than 4 are  :",filtered_values)

print("\nd. Convert the above result into set datatype.\n")

# considering the result mentioned in question is the result of filtured values.

new_set = set(filtered_values)

print("The result that is of values greater than 4 is converted to set :",new_set)

print("\ne. Make that set immutable.\n")

# to make a iterable like set , lists or dicstionaries immutable we use frozenset() function which
# accepts those iterables as arguments and returns a immutable object of the same form.

immutable_set = frozenset(new_set)
print("Set has been made immutable.")

print("\nf. Evaluate the maximum value from set and find out its hash value\n")
maximum_value = filtered_values[0]
for value in immutable_set :
    if value > maximum_value:
        maximum_value = value

print("Maximum value in  the set is ",maximum_value)

# Hash values are special type of coded values used to identify some values or strings or data and it changes as that data change .
# It is different if same value considered as different data type.

print("\nHash values for the  maximum value according to the considerration :")
print("if it is considered as a integer then :",hash(maximum_value))
print("if it is considered as a string then :",hash(str(maximum_value)))


#Q4
#Create a class named Student, use the_init_() function to assign
#values for name and roll number. And also call _del_() function to
#destroy object that is created.

print("\nQuestion 4. Function related to OOPs concepts .\n")
class student:
    def __init__(self): #it is called implicitly just after creating a object to assign some default values to attributes.
        self.name= input("Enter your name: ")
        self.roll_number = int(input("Enter your Roll number: "))
    def print_data(self):
        print("Name is :",self.name)
        print("Roll number is :",self.roll_number)
    def __del__(self): #it is called implicitly just before the end of program to delete the object.
        print("Object is destroyed")

kid = student() #creating a new object of student class
print()
kid.print_data()
print()

# since after everytime program is going to end __del__ function will be automatically called 
# so we dont need to call that manually.

#Q5.
# Write a program to store details of three employees: name and salary
# using class.



print("\nQuestion 5. To store  details of empoyees and update their info.\n")
class details:
    def __init__(self):
        self.details ={}
    
    def get_details(self,name,salary):
        self.details[name]= salary
    
    def update_salary(self,name,salary):
        if name in self.details :
            self.details[name]= salary
            print(f'\nSalary of {name} named person  is updated to {salary} !!!')
        else:
            print(f'{name} named person is missing in data !!!')

    def delete_details(self,name):
        if name in self.details :
            del self.details[name]
            print(f'record of "{name}" named person is deleted from data !!!')

        else:
            print(f'{name} named person is missing in data !!!')
    
    def print_record(self):
        print("{:<8}      {:<8}".format("Name","Salary"))
        print()
        for name,salary in self.details.items():
            print("{:<8}      {:<8}".format(name,salary))

       
data = details()
data.get_details("Mehak",40000)
data.get_details("Ashok",50000)
data.get_details("Viren",60000)

data.print_record()
data.update_salary("Mehak",70000)
print()
data.print_record()
data.delete_details("Viren")
data.print_record()

#Q6.Barbie and George are the two friends. On Saturday, they decided to
#   travel to a fair where they discovered a fun game that put their
#   friendship to the test. The test required George to utter a word and
#   Barbie to create a new meaningful word using the exact same letters
#   as George. If Barbie fails to form a word then their friendship is a fake.

print("\nQuestion 6. To check if friendship is true or not .\n")
george_word = input("Enter your word George :")
barbie_word = input("Enter your word Barbie and remember it must be consistig of same words as George word letters only :  ")

if len(george_word)==len(barbie_word):
    friendship=False
    for letter in george_word.lower():
        if letter not in barbie_word.lower():
            print("\nBarbie your word does not contain same  letters as George .")
            print("So your friendship is fake.")
            break
        else:
            friendship=True
    if friendship:
        print("\nBarbie your word  contains same  letters as George .")
        print("So your friendship is true.")
        
        
else:
    print("\nBarbie your word  deos not contain same  letters as George .")
    print("So your friendship is false.")




        
    

    
    
