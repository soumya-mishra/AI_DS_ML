# Python-ML
Python &amp; Machine Learning
#Regular expression 
import re
str = "Course location is London or Paris!"
mo = re.search(r"location.*(London|Paris|Zurich|Strasbourg)",str)
print(mo.group())
############################
#List comprehension
nums = [2,3,4,5,6,7.8,9,10]
my_lists = [n for n in nums if n%2==0]
print(my_lists)
###################
my_list = [(letter,n) for letter in 'abcd' for n in range(4)]
print(my_list)
############################
#Iterator
expertises = ["Novice", "Beginner", "Intermediate", "Proficient", "Experienced", "Advanced"]
expertises_iterator = iter(expertises)
next(expertises_iterator)
##########################
def city_generator():
    yield("London")
    yield("Hamburg")
    yield("Konstanz")
    yield("Amsterdam")
    yield("Berlin")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")
    
city = city_generator()
print(next(city))    
print(next(city))  
print(next(city))  
#####################
def fibonacci(n):
    """ A generator for creating the Fibonacci numbers """
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield b #you can yield a or b
        a, b = b, a + b
        counter += 1
f = fibonacci(10)
for x in f:
    print(x, " ", end="") # 
print()
#################
def infinite_looper(objects):
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        message = yield objects[count]
        if message != None:
            count = 0 if message < 0 else message
        else:
            count += 1

x = infinite_looper("soumya")            
