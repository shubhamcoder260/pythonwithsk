# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def sum(num_1,num_2):
    return num_1+num_2
print(sum(2,4))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.


def area_of_circle(r):
    area=3.17*r*r
    return area
print(area_of_circle(5))



# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*add):
    i=0
    for num in add:                 #impo#
        i+=num
        
    return i
print(add_all_nums(2,3,4,5))




# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.


def temp_conversion(c):
    f=(c * 9/5) + 32
    return f
print(temp_conversion(45))
    



# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month=='september'or'october'or'november':
        return 'its autmn'
    
    elif month=='december'or'january'or'february':
        return 'its winter'
    
    elif month=='march'or'april'or'may':
        return 'its spring'
    else:
        return 'its summer'
print('currently',check_season('january'))

# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1,x2,y1,y2):
    m=(y2-y1)/(x2-x1)
    return m
print('the slope is:',calculate_slope(1,2,3,4))


# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_equation(a,b,c):
    x=(-b + ((b*b)-4*a*c)**0.5)/2*a
    y=(-b - ((b*b)-4*a*c)**0.5)/2*a

    return (x,y)


print('the solution for the quadratic eqn is :',solve_quadratic_equation(1,4,1))






# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.


def print_list(a_list):
    for element in a_list:
        print(element)
print_list([1,2,3,4,5,6,7890,'fghj'])


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]


def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
                                                                        ### not complete ###
# Test the function
original_list = ['A','B','C','D']
reversed_list = reverse_list(original_list)
print("Original list:", original_list)
print("Reversed list:", reversed_list)

        



# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(small_list):
   small_list=str(small_list)
   small_list=small_list.capitalize()                                   ###not complete###
   return small_list
print(capitalize_list_items(['my','name','is','shubham','karn']))




# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]


# def add_item(list_param,item_param):
#     for items in range(len(list_param)):
#         list_param[items]+=item_param
    
#     return list_param
# print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'],' rice'))



# def add_item(food_staff,item):
#     food_staff.insert((len(food_staff)-1)+1,item)

#     return food_staff

# print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'],'meat'))




# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]

def remove_item(food_staff,item):
    food_staff.remove(item)

    return food_staff

print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'],'Mango'))




# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050


def sum_all_numbers(nums):
    total=0
    for num in range(1,nums+1):
        total+=num
    return total
print(sum_all_numbers(100))



# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.


def sum_all_oddnumbers(nums):
    total=0
    for num in range(1,nums+1,2):
        total+=num
    return total
print(sum_all_oddnumbers(6))


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_all_evennumbers(nums):
    total=0
    for num in range(0,nums+1,2):
        total+=num
    return total
print(sum_all_evennumbers(6))


# Exercises: Level 2


# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.

def even_and_odd(nums):
    for nume in range(0,nums+1,2):
        print(nume)
    for numo in range(1,nums+1,2):
        print(numo)
    
print(even_and_odd(100))


# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(fact):
    if fact==0:
        return 0
    else:
        return (fact*(fact-1))
print(factorial(4))





# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(emp):
    if emp==None:
        print('this variable is empty')
    else:
        print('not empty')
    return ''
print(is_empty('mass'))
    



# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).




# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.

    

# Write a functions which checks if all items are unique in the list.


def unique(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]==lst[j]:
                return 'the given list do not have unique characters'
            
    return 'the given list has unique characters'
print(unique([1,2,3,4,6]))




# Write a function which checks if all the items of the list are of the same data type.


def type_checker(samp_list):
    for i in range(len(samp_list)):
        a=str(type(i))
        print(a)
        for j in range(i+1,len(samp_list)):
            b=str(type(j))
            print(b)
            if a==b :
                return ('the list has items with same data types ')
print(type_checker([1,2,3,4,5,6,'45']))

# Write a function which check if provided variable is a valid python variable


def var_check(par):
    a=type(par)
    if a ==str or list or tuple or set or dict or int or float:
        print('the given parameter is fine')
    else:
        print('not fine')
print(var_check([1,2,4,'g',2,4,5,6,78,8]))


# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
