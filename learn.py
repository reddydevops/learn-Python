print("Hello World")

print(f"20 days to learn Python are {20 * 24} hours")

print("Python is fun" + ", Python is cool" + ", I love Python")

calc_to_mins = 24 * 60
name_of_unit = minutes = "minutes"
print(f"20 days are {20 * calc_to_mins} { name_of_unit }")


def days_to_units():
    print(f"20 days are {20 * calc_to_mins} { name_of_unit }")

days_to_units()

def days_to_units(num_of_days,msg):
    var= 10
    print(f"{num_of_days} days are {num_of_days * calc_to_mins} { name_of_unit }")
    print(msg)

days_to_units(20,"That's a lot of minutes!")

# user input

def days_to_units(num_of_days):  
    if(num_of_days>0):  
        return (f"{num_of_days} days are {num_of_days * calc_to_mins} { name_of_unit }")
    elif(num_of_days==0):
        return "You entered a 0, please enter a positive number"
    else:
        return "You entered a negative number"

user_input = input("Enter number of days and I will convert it to minutes\n")
#user_input_days = int(user_input) type(vale)
if(user_input.isdigit()):
    value = days_to_units(int(user_input))
    print(value) 
else:
    print("You entered a string, please enter a positive number")


print(type(30.88))

#Conditionals
"""def validate():
    if(user_input.isdigit()):
        user_input_number = int(user_input)
        if(user_input_number>0):              
            calculation = days_to_units(user_input_number)
            print(calculation)    
        elif user_input_number == 0 :
            print ("You entered a 0, please enter a positive number")
        else:
            print ("You entered a negative number")

user_input = input("Enter number of days and I will convert it to minutes\n")
validate() """

#Loops
def validate():
    try:
        user_input_number = int(no_of_days)
        if(user_input_number>0):              
            calculation = days_to_units(user_input_number)
            print(calculation)    
        elif user_input_number == 0 :
            print ("You entered a 0, please enter a positive number")
        else:
            print ("You entered a negative number")
    except ValueError:
        print ("Your input is not valid number")

user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter number of days and I will convert it to minutes\n")
    for no_of_days in set(user_input.split(",")):
        validate()

#sets
myset = {"queue","stack","array","list","tuple"}
for i in myset:
    print(i)

myset.add("set")
print(myset)

[3,5,7].count()

fruits = ["apple","banana","cherry","kiwi","mango"]
print(fruits[1])
print("last fruit:",fruits[-1])
print(fruits[0:2]) #slicing
fruits[0] = "orange"
# Create a new list with fruits containing the letter 'a'
newlist = []
newlist = [x for x in fruits if "a" in x]
print(newlist)
#sort
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#loop
for x in fruits:
    print(x)

num = (1,2,3,4,5)
for x in num:
    print(x)

person_info = {"first_name":"John",
               "age":"22",
                "city":"New York"}
print(person_info["first_name"])
my_dict = dict(name = "John", age = 36, country = "Norway") 
print(my_dict.get)
my_dict.keys()
my_dict.values()    
for x,y in person_info.items():
    print(x,y)

new_dict = person_info.copy()
new_dict.update({"email":"xyz"})
print(new_dict)
new_dict.pop("age")
new_dict.setdefault("address","25-90-1234")
print(new_dict)

#functions
def my_function(fname,lname):
    print(fname + " " + lname)
my_function("John","Doe")

def add(x,y):
    return x+y
result = add(5,3)
print(result)

def multiply(x,y=5):
    return x*y
multiply(3)
print(multiply(3))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def addition(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(addition(5,10,15,20))

def greet(name):    
        print("Hello " + name)
greet("John")

def mname(*names):
    for name in names:
        print(name)
mname("John","Doe","Smith")

def person(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
person(name="John", age=30, city="New York")

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))


name="John"
coin= 5
msg= "\nHello {} you have {} coins".format(name,coin)
print(msg)

if __name__ == "__main__":
    validate()
    print("This is executed when the script is run directly")