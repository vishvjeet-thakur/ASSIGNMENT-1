#                                                            ASSIGNMENT 3


print("                                                      ASSIGNMENT 3 ")

#QUESTION 1

# Write a Python program to count the number of occurrences of each word or
# character in the string entered by the user. (Count the Number of Occurrences
# of each character only if the single word is entered by the user).

# As mentioned in the question that we have to check for the number of same words 
#so considering ABc same as abC means case independent......

print("Question 1 :  To count the number of words in a string or characters . \n")

input_str = input("Enter a string : ")
str = input_str.lower()
word_list = [x.strip() for x in str.split()]

num_words ={}
if len(word_list)==1:
    print("Since word length is 1 so checking for the number of same  characters :")
    for ch in word_list[0]:
        if ch not in num_words:
            num_words[ch]=1
        else:
            num_words[ch]+=1
else:
    print("Since word length is greater than 1 so checking for the number of same words :")
    for words in word_list:
        if words not in num_words:
            num_words[words]=1
        else:
            num_words[words]+=1

for word in num_words:
    print("{:<13}:{:<10}".format(word,num_words[word]))









#QUESTION 2

# Write a python script to print next date of input date. It must meet following
# conditions(use if-elif).

print("\n\nQuestion 2:- To print the next date of input date .\n")

year_ok = False

while  ( year_ok==False ) :
    year = int(input("Enter  year -"))
    if (year<=0  ) :
        print("Please input valid year !!!!!!")
    else:
        year_ok = True
leap_year =False
if(year%4==0):
    leap_year =True

month_ok = False
while  ( month_ok==False ) :
    month = int(input("\nEnter month -"))
    if (month<=0 or month>=13  ) :
        print("Please input valid month !!!!!!")
    else:
        month_ok = True

day_30_month = [4,6,9,11]

day_ok = False
while  ( day_ok==False ) :
    day =  int(input("\nEnter day -"))
    if (day<=0 or day>31) :
        print("Please input valid day !!!!!!")
    elif (leap_year==False and month==2 and day>28 ):
        print("\nYear you entered is  not a leap year . \n So February cannot have more than 28 days !!!!! \nPlease enter correct day again ")
    elif (leap_year and  month==2 and day>29 ):
        print("\nYear you entered is a leap year .\nSo February cannot have more than 29 days !!!!! \nPlease enter correct day again ")
    elif(month in day_30_month and day>30):
        print("\nMonth you have entered has not  more than 30 days!!!!! \nPlease enter the valid day ")
    else:
        day_ok = True

if((leap_year and month ==2 and  day==29 ) or (leap_year==False and month ==2 and day==28)):
    next_day = 1
    next_month =month+1
    next_year = year
elif(month in day_30_month and day==30):
    next_day = 1
    next_month = month+1
    next_year = year
elif(month ==12 and day==31):
    next_day = 1
    next_month =1
    next_year = year+1
elif(month not in day_30_month and day==31):
    next_day = 1
    next_month =month+1
    next_year = year
else:
    next_day = day+1
    next_month =month
    next_year = year
if(month<10):
    print("\n\nEntered date is : {}/0{}/{}\n".format(day,month,year))
else:
    print("\n\nEntered date is : {}/{}/{}\n".format(day,month,year))
if(next_month<10):
    print("Next date is : {}/0{}/{}\n".format(next_day,next_month,next_year))
else:
    print("Next date is : {}/{}/{}\n".format(next_day,next_month,next_year))



# Question 3 
# Write a Python program to create a list of tuples with the first element as the
#  number and Second element as the square of the number.

print("\n\nQuestion 3: to create a list of tuples having first element as the number and second as the square of the number. \n")
list_numbers = [int(x) for x in input("Enter all the numbers in a single line separated by space : ").split()]

new_list = []

for num in list_numbers :
    new_tuple =(num,num**2)
    new_list.append(new_tuple)

print("New list is :\n",new_list)

# Question 4 :
# Write a program to prompt the user for a grade between 4 and 10. If the grade
# is out of range print error message. If the grade is between 4 and 10 Print the
# grade.

print("\n\nQuestion 4: To print the grade and remark according to his/her grade .  \n")
grade_dict={
             10:("A+","outstanding"),
             9:("A","Excellent"),
             8:("B+","Very Good"),
             7:("B","Good"),
             6:("C+","Average"),
             5:("C","Below Average"),
             4:("D","Poor")
           }

print("Grade distribution is as :\n")
print("{:<15}{:<20}{:<15}".format("Letter Grade","Performance","Grade Point "))
for number,letter  in grade_dict.items():
    print("{:<15}{:<20}{:<15}".format(letter[0],letter[1],number))

# checking whether input given is valid or not .

grade_ok =False
while grade_ok == False :
    grade = int(input("\nEnter your grade between 4 to 10 : "))
    if(grade > 10 or grade <4):
        print("Grade must be between 4 to 10 !!!! \n please enter a valid grade : ")
    else:
        grade_ok = True

print("\nYour Grade is {} and {} Performance.".format(*grade_dict[grade]))



# Question 5 
# Pattern Printing

print("\n\nQuestion 5: Pattern printing.\n")
Ascii_A = ord("A") # ord() function returns the ASCII value of the character 

for line in range(6):
    print(" "*(line),end="") # it can be shown that the number of whitespaces at the beggining of the line is equal to the line number starting from 0.
    for char_num in range(11-(2*line)):
        print(chr(Ascii_A + char_num),end="") # chr() function returns the character correspionding to a ASCII Value.
    print()
    




# Question 6
# Write a python script that repeatedly ask user to enter name and SID of
# students (use ‘Y’ or ‘N’). Store them in a dictionary whose keys are SID’s and
# values are student’s name.


#*************************************************************************************
#  Using Dictionary functions 
# In the previous version of python , Dictionary was unordered so according to those version it couldn't be sorted
# But in the latest version we can sort that as it is ordered now.
# Dictionary functions like 
# items() - returns key, value pairs in the form of iterable so we can acces them using 'in' keyword.
# keys() - returns the list of keys
# values() - returns the list of values 
#**************************************************************************************


# accepting input and checking whether user gave correct input

print("\n\nQuestion 6 : Dictionary functions and sorting.\n")
program_flow = True
user_data={}
while(program_flow):
    student_name = input("Enter name : ")
    input_ok = False
    while(input_ok == False):
        student_sid = input("Enter  SID  :")
        if student_sid.strip().isdigit():
            input_ok = True  
        else:
            print("\nSID can only be a combination of numbers!!! ")
        
    user_data[student_sid]=student_name
    str = "k"
    while(str.lower()!="y" and str.lower()!="n"):
        str=input("\nDo you want to store more student data (Y/N) : \n")
        if str.lower()=="n":
            program_flow = False
        elif str.lower()!="y" :
            print("\nPlease enter Y or N only!!!\n")
    
# a. Print students details stored in the dictionary.

print("\nStudent data in the order as entered by the user : ")
for student_sid , student_name in user_data.items() :
    print(student_sid," : ",student_name)

# b. Sort dictionary using student names.
sorted_names = sorted(user_data.values())
new_user_data ={}
for student_name in sorted_names:
    for student_sid , names in user_data.items():
        if(names==student_name):
            new_user_data[student_sid]=student_name

print("\nSorted dictionary according to student names :")
for student_sid ,student_name  in new_user_data.items() :
    print("{:<15}:{:<15}".format(student_sid,student_name))

# c. Sort dictionary using student sids.

sorted_sids = sorted(user_data.keys())
new_user_data ={}
for student_sids in sorted_sids:
    for student_sid , student_name in user_data.items():
        if(student_sid==student_sids):
            new_user_data[student_sid]=student_name

print("\nSorted dictionary according to student sids :")
for student_sid,student_name in new_user_data.items() :
    print(student_sid," : ",student_name)

# d. Search a student details with SID and print name of that student.

input_ok = False
while(input_ok == False):
    search_sid = input("\nEnter the SID whose name you want to search :")
    if search_sid.strip().isdigit():
        input_ok = True
    else:
        print("\nSID can only be a combination of numbers!!! ")

if search_sid in user_data:
    print("\nName of the student with SID {} is {}.".format(search_sid,user_data[search_sid]))
else:
    print("SID {} is not present in our data.".format(search_sid))
    

#    Question 7.
#    Write a python program to print Fibonacci sequence also print Average of the
#    resultant Fibonacci series.
       
    
#***********************************************************************************************************************
# Using Recursion of functions which is basically function calling itself but we can also do this using simply loops.
# Printing Fibonacci series according to the input user will give the number of terms he want the series.
# Fibonacci series  - 1,1,2,3,5,8,13....
#***********************************************************************************************************************


# Fibonacci function which will print the series and return the sum of all the terms of the series.

print("\n\nQuestion 7 :  Printing of Fibonacci series .")

def Fibonacci(num,sum=0,last=1,second_last=1):
    if last==1 and second_last==1:         #  function will first start from this block  as initially no argument will be passed for last and second_last.
        print(second_last,last,end=" ")
        sum=sum+2
        temp = last
        last = last + second_last
        second_last = temp
        num-=2
        Fibonacci(num,sum,last,second_last)
        return sum   # returning sum which will be used for calculating average.
    elif num>0:
        print(last,end=" ")
        sum=sum+last
        temp = last
        last = last + second_last
        second_last = temp
        num-=1
        Fibonacci(num,sum,last,second_last)
        return sum

# checking for the input if number of terms is a integer and greater than 0.

input_ok = False
while input_ok == False:
    num = input("Enter the number of terms to which you want the Fibonacci Series :")
    if num.strip().isdigit():
        num =int(num)
        if(num<=0):
            print("Numbers of terms cannot be less than 0 !!!")
        else:
            input_ok = True
    else:
        print("Numbers of terms can only be a  number not a alphabet !!!")
print()
sum = Fibonacci(num) # accepting the value returned by the Fibonacci function.
avg = sum/num
print("\n\nAverage is ",avg)


# Question 8.
# Given the sets below, write python statement to:
# Set1= {1, 2, 3, 4, 5}
# Set2= {2, 4, 6, 8}
# Set3= {1, 5, 9, 13, 17}
print("\n\nQuestion 8 :  Set methods -  union , intersection , difference .")
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

print("Given sets are :")
print("Set1 = ",Set1)
print("Set2 = ",Set2)
print("Set3 = ",Set3)


#****************************************************************
# We can use |(or) operator or union method on sets to find Union.
# We can use &(and) operator or Intersection on sets to find Intersection.
# We can use -(difference )  operator  for Difference between sets.
#****************************************************************




# a. Create a new set of all elements that are in Set1 and Set2 but not both.

new_set = Set1.union(Set2) - Set1.intersection(Set2)
print("\nNew set of all elements that are in Set1 and Set2 but not both : ", new_set)

# b. Create a new set of all elements that are in only one of the three sets Set1, Set2 and Set3.

unique_element_set = (Set1|Set2|Set3) - (Set1 & Set2)-(Set2 & Set3) - (Set3 & Set1)
print("\nNew set of all elements that are in only one of the three sets Set1, Set2 and Set3 :",unique_element_set)

# c. Create a new set of elements that are exactly two of the sets Set1, Set2 and Set3.  

exactly_two = (Set1 & Set2)|(Set2 & Set3)|(Set3 & Set1)-(Set1 & Set2 & Set3)
print("\nNew set of elements that are exactly two of the sets Set1, Set2 and Set3 : ",exactly_two)

# d. Create a new set of all integers in the range 1 to 10 that are not in Set1.

set_in_range = set(x for x in range(1,11)) - Set1
print("\nNew set of all integers in the range 1 to 10 that are not in Set1 :", set_in_range)

# e. Create a new set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3.

new_set_in_range = set(x for x in range(1,11)) - (Set1|Set2|Set3)
print("\nNew set of all integers in the range 1 to 10 that are not in Set1,Set2 and Set3:",new_set_in_range)

   
    
   

    

