# Exercises: Level 1


# Declare an empty list
list=[]

# Declare a list with more than 5 items
listt=['apple','mango','banana','guava','orange']

# Find the length of your list
print('length of list is :',len(listt))


# Get the first item, the middle item and the last item of the list

print(listt[0])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types=['shubham','19',"5'9",'unmarried','birgunj']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook',' Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

# Print the list after modifying one of the companies
it_companies[0]='boat'
print(it_companies)
# Add an IT company to it_companies
print(it_companies.append('IT company'))
print(it_companies)


# Insert an IT company in the middle of the companies list

print(it_companies.insert(4,'fintech'))

print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[4]=it_companies[4].capitalize()
print(it_companies)

# Join the it_companies with a string '#;  '
print('#; '.join(it_companies))



# Check if a certain company exists in the it_companies list.

print( 'cosco' in it_companies)
# Sort the list using sort() method

# it_companies=['Facebook',' Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']

# it_companies.sort()
# print(it_companies)

# Reverse the list in descending order using reverse() method
# print(it_companies)

# Slice out the first 3 companies from the list

print(it_companies[:3])

# Slice out the last 3 companies from the list
print(it_companies[6:])

# Slice out the middle IT company or companies from the list
middleindex=len(it_companies)//2
middleindex=it_companies.pop(middleindex)
print(middleindex)

# Remove the first IT company from the list
firstIT=it_companies.pop(0)
print(firstIT)


# Remove the middle IT company or companies from the list

middleindex=len(it_companies)//2
middleindex=it_companies.pop(middleindex)
print(middleindex)

# Remove the last IT company from the list
it_companies=['Facebook',' Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']

print(it_companies.pop(6))



# Remove all IT companies from the list

print(it_companies.clear())


# Destroy the IT companies list
del it_companies
# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack=front_end+back_end
print(full_stack)



# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack=full_stack.copy()
full_stack.insert(8,'sql')
full_stack.insert(10,'redux')
full_stack.insert(9,'python')
print(full_stack)

# Exercises: Level 2




# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)

# Add the min age and the max age again to the list

min_age=ages[0]
n=len(ages)
print(n)
max_age=ages[n-1]
result=min_age+max_age
print(result)

# Find the median age (one middle item or two middle items divided by two)
lislen=len(ages)
median_age=lislen/2
median_age=median_age
print('the median age index is:',median_age)
median_age=int(median_age)
print(ages[median_age])

median_age=len(ages)
median_age=int(median_age)
if median_age%2==1:
    print('median age is:',ages[median_age])
else :
    ages[median_age//2-1]+ages[median_age//2]
    print('median age is:',ages[median_age//2-1]+ages[median_age//2])
# Find the average age (sum of all items divided by their number )
    sum=(ages[0]+ages[1]+ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9])/len(ages)
    print(sum)
# Find the range of the ages (max minus min)
    range=(ages[0]+ages[9])/2
# Compare the value of (min - average) and (max - average), use abs() method
    
# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.