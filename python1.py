print("Hello World")

# ##Variables
age = 20
price = 19.95
first_name = "Lynn"
is_online = False

# ##Exercise name is John Smith, age is 20, new_patient
first_name = "John"
Second_name = "Smith"
age = 20
patient = "new_patient"

print(first_name,Second_name,age,patient)
 
# ##Receiving input from user
name =input("what is your name?")
print("Hello" + "", name) 

# ##type conversion
birth_year = (input("Enter your birth year"))
age = 2020 - int(birth_year)

# ##we only concatenate strings
print("You are " + str(age) + "", "years old")

#printing sum of two numbers

number1 = int(input("input any number: "))
number2 = int(input("input another number: "))
sum = float(number1 + number2)

print("Sum:" + str(sum))

#Strings
course = "python for beginners"
print(course.upper()) ##concerting a string to upper case
print(course.find("for"))##prints the index of letter y
print(course.replace("for", "4"))## replacing strings
print(course.find('python')) ## checking for string
print('python' in course)
 
##Arithmetic operations
print(10 + 3)
print(10/3)
print(10 // 3) ## get an integer
print(10 % 3) ## gives you the remainder 
print(10**3) ##gives you the power

x = 10 
x += 3 ##aurgmented operators

print(x)

x = 10 + 3 * 2
print(x)

#Comparison values(!=, >, <, >=, <=)
x = 3 == 2
print(x)

##Logical operators
price = 20

print(price > 10 and price < 30) ##both have to be correct
print(price > 10 or price < 30) ##as long as one is correct
print(not price > 10) ##gives you the vise of the answer

## three logical operators and,or, not

#if statements
#are used to make decisions
temperature = 24

if temperature > 30:
    print("Its a hot day")
    print("Drink hot water")

elif temperature > 20: ##(Greateer than 20 and less than 30)
    print("Its a nice day")

elif temperature > 10: ##( > 10 and less than 20)
    print("its abit cold")

else:
    print("its cold")

#exercise
#enter weight
#is it in kg  or l

weight = int(input("please input your weight: ")) 
measure = (input("is your weight in (K)g or (L)bs: "))

if measure.upper() == "K":
    converted = weight / 0.45
    print("Your weight in Lbs: " + str(converted))
elif measure.upper() == "L":
    converted = weight  * 0.45
    print("Your weight in Kgs: " + str(converted))
else:
    print("Please input the correct value of K or L")


#while loops are used to repeat a block of code a number of times
i = 1
while i <= 10:
    print(i * '*')
    i = i + 1

 #Lists
names = ["Lynn", "Amoit","Paula","Bridget"]
print(names)
names[0] ="Lynette"
print(names[0:2]) ##prints index 0 and 1 
print(names[-1])

print(names)

##List methods
##Adding numbers to a list
numbers = [1,2,3,4,5]
numbers.append(6) ##add digit 6 a the end of the list
numbers.insert(1, -5) ## to insert a new number at any index

numbers.remove(3) ## remioves the number 3

# numbers.clear() ## removes everything from the list

print(len(numbers)) #3Checks the length of numbers

##For loop
numbers = [1,2,3,4,5,6]
for i in numbers:
    print(i)


i = 0
while i <= len(numbers):
    print(numbers[i])
    i = i + 1

##The range function is used to generate a sequence of numbers
#numbers = range(10, 20, 2) ##The third number is a step for the next number
for number in range(5):
    print(number) ##prints numbers 0-10

##Tuples we use them to store a sequence of lists
##they cant be changed hence immutable
numbers = (1,2,3) ##immutable r unchangeable we cant append or even do anything

##Create a for loop that gives you a multiples of 2
i = 2
while i <= 20:
    print(i)
    i += 2

for i in range(2,20,2):
    print(i)
