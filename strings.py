# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

a='thirty '
b='days '
c='of '
d='python'
print(a+b+c+d)


# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.





                      # SAME AS ABOVE  #





# Declare a variable named company and assign it to an initial value "Coding For All".


company='Coding for all'

# Print the variable company using print().

print(company)

# Print the length of the company string using len() method and print().

print(len(company))


# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())


# Cut(slice) out the first word of Coding For All string.

print(company[7:15])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(company.index('Coding'))


# Replace the word coding in the string 'Coding For All' to Python.


print(company.replace('Coding','Python'))
# Change Python for Everyone to Python for All using the replace method or other methods.


str1='Coding for all'
str2=str(company.replace('Coding for all','Python for all'))
print(str1,str2)

# Split the string 'Coding For All' using space as the separator (split()) .

print(company.split(' '))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

comp="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(comp.split(','))


# What is the character at index 0 in the string Coding For All.

print(company[0])




# What is the last index of the string Coding For All.

print(company[13])
# What character is at index 10 in "Coding For All" string.

print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.

abb=str2[0]+str2[7]+str2[11]
print(abb.upper())

# Create an acronym or an abbreviation for the name 'Coding For All'.

    #save the string and same logic as above#

# Use index to determine the position of the first occurrence of C in Coding For All.

print(company.index('C'))


# Use index to determine the position of the first occurrence of F in Coding For All.

#SAME AS ABOVE#

# Use rfind to determine the position of the last occurrence of l in Coding For All People.

print(company.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

bec='You cannot end a sentence with because because because is a conjunction'
print(bec.find('because'))



# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(bec.rfind('because'))


# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(bec[31:54])


# Does ''Coding For All' start with a substring Coding?

print(company.startswith('Coding'))
# Does 'Coding For All' end with a substring coding?

print(company.endswith('Coding'))


# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

txt='    Coding For All    '
print(txt.strip('    '))

# Which one of the following variables return True when we use the method isidentifier():

#     30DaysOfPython
#     thirty_days_of_python
two='thirty_days_of_python'
one='30DaysOfPython'
print(one.isidentifier())
print(two.isidentifier())


'# '

###  IMP  ### The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

lis='Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'
print('# '.join(lis))



# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge \nI just wonder what is next.')


# Use a tab escape sequence to write the following lines.

# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

tab='''Name     \t  Age  \t   Country \t  City
Asabeneh     \t 250  \t   Finland \t  Helsinki'''
print(tab)




                                                                   ###LATER###



#     Use the string formatting method to display the following:

# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.


                                

#     Make the following using string formatting methods:

# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

