
def median(num):
    no=len(num)
    if no % 2 ==1:
        n=(no-1)//2
        print(num[n])
    else:
        mid1=len(num)//2
        mid2=mid1-1
        print((num[mid1]+num[mid2])/2)
        

print(median([1,2,3,4]))


# Write a program that takes a number as input and prints its factorial.

num=int(input('enter a number'))
fact=1
if num<1:
    print('the factorial is not defined')
else:
    for n in range(1,num+1):
        fact *= n
        
    print(fact)






# Create a program that generates a random password of a specified length using lowercase letters, uppercase letters, and digits.




# Variables:

# Write a program that calculates the area and perimeter of a rectangle given its length and width using variables.
    



# Create a program that converts a given amount of money from one currency to another using variables to store exchange rates.

cur=input('choose your currency [ind,nep]\n')
if cur == 'ind' :
    irs=float(input('enter the amt in ind rs'))
    print('calculating.........\n')
    print('your currency is converted into nrs\n amount is :',(1.6)*irs)
elif cur == 'nep':
    nrs=float(input('enter the amt in nep rs'))
    print('your currency is converted into irs\n amount is :',nrs/(1.6))

# Built-in functions:

# Write a program that sorts a list of numbers in ascending order using the sorted() function.
# Create a program that takes a string as input and counts the occurrences of each character using the count() function.
# Operators:

# Write a program that calculates the square root of a given number without using the sqrt() function.
# Create a program that checks if a given year is a leap year or not using logical operators.
# Strings:

# Write a program that checks if a given string is a palindrome ignoring spaces and punctuation.
# Create a program that capitalizes the first letter of each word in a given sentence.
# Lists:

# Write a program that merges two sorted lists into a single sorted list.
# Create a program that finds the mode (most frequent element) in a list of numbers.
# Tuples:

# Write a program that calculates the dot product of two vectors represented as tuples.
# Create a program that takes a list of tuples representing student names and their scores, and returns the student with the highest score.
# Conditionals:

# Write a program that determines the type of a triangle (equilateral, isosceles, or scalene) based on the lengths of its sides.
# Create a program that simulates a simple calculator with addition, subtraction, multiplication, and division operations using conditional statements.
# Loops:

# Write a program that prints all prime numbers between 1 and 100 using a for loop.
# Create a program that calculates the factorial of a given number using a while loop.
# Functions:

# Write a function that takes a list of numbers as input and returns the sum, average, maximum, and minimum.
# Create a function that checks if a given string is a pangram (contains every letter of the alphabet at least once).
    











#swap first and last element in a list
def swaplist(list):
    lenth=len(list)
    temp=list[0]
    list[0]=list[lenth-1]
    list[lenth-1]=temp
    return list
print(swaplist([1,2,3,4,5,6]))


def swaplist2(list2):
  list2[0],list2[-1]=list2[-1],list2[0]
  return list2
print(swaplist2([1,2,3,4,55,66,77]))


def swaplist3(list3):
  first=list3.pop(0)
  last=list3.pop(-1)
  list3.insert(0,last)
  list3.append(first)
  return list3
print(swaplist3([1,2,33,44,5,66,900]))

    



# def swaplist(list):
#         lenth=len(list)
#         temp=list[0]
#         list[0]=list[lenth-1]
#         list[lenth-1]=temp
#         return list
# print(swaplist([1,2,3,4,5,6]))

# def swaplist2(list2):
#   list2[0],list2[-1]=list2[-1],list2[0]
#   return list2
# print(swaplist2([1,2,3,4,55,66,77]))

# def swaplist3(list3):
#   first=list3.pop(0)
#   last=list3.pop(-1)
#   list3.insert(0,last)
#   list3.append(first)
#   return list3
# print(swaplist3([1,2,33,44,5,66,900]))

#paliindrome
# def slicc(pal):
#   print('this statement is: ',pal==pal[::-1])

# c=str(input('enter a word: '))
# print(slicc(c))

# def strings(para1,para2):
#   if para1 in para2:
#     print('YES')
#   else:
#     print('NO')
# let=str(input('enter a word'))
# let2=str(input('enter second word'))
# print(strings(let,let2))

#two string can be rearranged to form one another
# def strings(para1,para2):
#   para1,para2=list(para1),list(para2)
#   for a in para1:
#     if a in para2:
#       print('yes')
#       break
#     else:
#       print('no')
# let=str(input('enter a word'))
# let2=str(input('enter second word'))
# print(strings(let,let2))

# def list(list1):
#   list2=list1.sort()
#   if list1 is list2:
#     print('sorted bro')
#   else:
#     print('bt')
#     return 'try again'

# print(list([1,2,3,45,4,56,5,67,78,7,89,89,90,7]))
