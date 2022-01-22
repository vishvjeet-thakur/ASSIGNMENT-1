

                                                                 #ASSIGNMENT 2
print("                                                          #ASSIGNMENT 2")

#QUESTION 1:

print("\nQUESTION 1 ")

str="Python is a case sensitive language"   #Given string

print("\n Given string is  :  ",str)

# a. lenth of the string
print("\n a.  Lenth of the string is :  " ,len(str))

# b. Reverse the order of the string in one line code
print("\n b.  Reversed string is : ", str[::-1])

# c. Using Slice function store “a case sensitive” in new string.

new_str = str[10:26]
print("\n c. 'a case sensitive ' stored in a new string ")

# d. Replace “a case sensitive” with “object oriented”.

replaced_str = str.replace(new_str,"object oriented")
print("\n d. String after replacement of '%s' with '%s' : "%(new_str,"object oriented"),replaced_str)

# e. Find index of substring “a” in the given input string.

print("\n e. Index of 'a' in the given input string :",str.index("a"))

# f. Remove the white spaces from the given input string.

removed_spc = str.replace(" ","")
print("\n f. After removing white spaces from the input string : ",removed_spc)


#QUESTION 2


# Store your name, SID, department name and CGPA into different variables

print("\nQUESTION 2")

name ="Vishvjeet Thakur"
SID = 21105066
department_name = "Electronics and Communication Engineering "
CGPA = 10.0

output_str ="""\n Hey, %s Here!
 My SID is %d
 I am from %s department and my CGPA is %.1f """

print(output_str %(name,SID,department_name,CGPA))


#QUESTION 3. Bitwise calculations

print("\nQUESTION 3")
#given data
a=56
b=10

#a. bitwise and (&)

print("\n\n a.  a&b : ",(a&b))

#b. bitwise or (|)

print("\n b.  a|b : ",(a|b))

#c. bitwise xor (^)

print("\n c.  a^b : ",(a^b))

#d.  bitwise left shift (<<) with 2 bits

print("\n d.  a<<2 : ",(a<<2),"\n     b<<2 : ",(b<<2))

#e.  bitwise right shift (>>) 

print("\n d.  a>>2 : ",(a>>2),"\n     b>>4 : ",(b>>4))



#  QUESTION 4. Write a python program to find the greatest of three numbers entered by the  user.

print("\nQUESTION 4")

p = [int(x) for x in input("\nEnter three numbers separated by space :   ").split()] #splts string by space and store that in a list

p.sort() # sorts in ascending order
print("Greatest of three numbers you entered is : ",p[2])



#QUESTION 5. Write a python program to check if the word “name” is present in the string entered by the user (Print : “Yes” or “No”)

print("\nQUESTION 5")

check_str = input("\nEnter a string to find if it contains 'name' or not  :  " ).split()
word = "name"
if word in check_str :
    print("Yes")
else:
    print("No")


#QUESTION 6. For any three lengths, there is a simple test to see if it is possible to form a 
#            triangle. If any of the three lengths is greater than the sum of the other two, 
#            then you cannot form a triangle. Otherwise, Enter three sides of a triangle, sT
#            converts them to integers, and to check whether the given input lengths can 
#            form a triangle or not (Print : “Yes” or “No”)


print("\nQUESTION 6")
sides = [int(x) for x in input("\nEnter three sides  separated by space to check whether we can form a triangle with them or not :  ").split()]

sides.sort()
if (sides[0]+sides[1])>sides[2]:
    print("Yes")
else:
    print("No")
