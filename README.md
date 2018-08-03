# Python
Complete Python bootcamp to learn python for data science, machine learning and AI.

## Python2 Vs Python 3
Choosing between Python 2 and Python 3 is difficult because many companies still had legacy Python2 code to be maintained. However Python 2 will stop receiving the security updates in year 2020. Many of the packages for Pyathon are already migrated to Python 3. Python 3 is the future of Python programming language.

[Nice Summary of the differences](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html)

[Site that tells you which packages are Python 3 compatible](http://py3readiness.org/)

## Python overview
It was developed by Guido van Rossum in 1991. Python uses indentation instead of curly braces to mark the block of code, so it typically involves less code. Many open source packages available.

## Installing Python
We will use Anaconda distribution package for installing Python, because it comes with python as well as many other standard packages including Jupyter. There is also Miniconda for installing smaller number of packages if we have less space.

Goto - https://www.anaconda.com/download/

Once installed, open Anaconda navigattor. This will show a dashboard of all the packages and tools that comes with Anaconda. We can use Jupyter,R studio and many more.

## Development environments
There are 3 main types of environments -
1. Text Editors
**Sublime and Atom** with packages for syntax highlighting and autocompletion.

2. Full IDEs - 
**PyCharm and Spyder**

3. Notebook environments
Notebooks are special file formats(**.ipynb**) that are not **.py** extentions. We can see input and output next to eachother. Supports inline markdown notes, visualations, videos and more. Most popular is the Jupyter Notesbook. We can use Anaconda navigator to launch the Jupyter notebook.

## Data Types
Basic building blocks for creating objects and data structures

Name | Type | Description
------------ | ------------- | -------------
Integers | int | Whole numbers: 3 300 200
Floating point | float | Numbers with decimal points: 89.83 4.7
Strings | str | Ordered sequence of characters: "hello", "Jane"
Lists | list | Ordered sequence of objects: [10,"hello",100.20]
Dictionaries | dict | Unordered key-value pairs: {"mykey":"value","name":"Jone"}
Tuples | tup | Ordered **immutable** sequence of objects: (10,"hello",100.20)
Sets | set | Unordered collection of **unique** objects: {"a","b"}
Boolean | bool | Logical value indicating True or False

Python 3 performs true division by default!

## Variables

1. Cannot start with numbers
2. Cannot use spaces, use _ instead
3. best practice to use lowercase
4. best preactice to avoid using keywords like list, str

Python uses **Dynamic typing** which allows us to reassign variables to different data types. This makes python very felxible in assigning data types, this is different than other languages that are **Statically-typed**

    my_dogs = 2

    //You can reassign them to list
    my_dogs = ["Rammy", "Tammy"]

**Pros of Dynamic typing**   
    - very easy to work with  
    - faster development time   

**Cons of Dynamic typing**   
    - May result in bugs for unexpected data types   
    - You need to be aware of **type()** function to check the data type.

## Strings  - str
Strings are order sequences of characters. As strings are order sequences we can use **indexing or slicing** to grab the sub sections of the string.   

**Indexing** - Indexing allowes you to get single characters from the string. Index start at 0 position. We can also use **reverse  indexing** which start at -1 to get last character from string. We use reverse indexing when we dont know the length of the string.

```
Character    - h  e  l  l  o
Index        - 0  1  2  3  4
Reverse Index- 0 -4 -3 -2 -1
```

**Slicing** -  Slicing allows you to grab a sub section of multiple characters, a slice of a string. Following syntax -   

**[start:stop:step]**   

**Start** is numerical index for the slice start   
**stop** index you will go upto but not include    
**step** size of the jump you take. Default jump size is 1.

**len(str)** - It allows to get the length of the string.  
**capitalize()** - Capitalize the first letter in string.

**1. Properties of String**   
- Immutability - Strings are immutable in nature. You can't use indexing to change individual elements of a string.   
- Concatenation - Supports concatenation using + operator   
- Multiplication - * to print number of type   

**2. Methods**   
Various build methods like upper(), lower(), count(), find(), split() - Default split by space, otherwise pass the split regex etc

**3. Print formatting with Strings**    
There are multiple ways to format string for printing variables in them, this is called as **interpolation.**  

**.format()** -   
**f-strings**(formatted string literals) - 

Awesome source for print formatting - https://pyformat.info/   


## Lists - list  
Lists are order sequences that can hold variety of object types. They use brackets[] and commas to separate objects in the list, [1,2,3,4]. List supports **indexing and slicing**.

They are similar to Strings like we can contact 2 list using + operator, can do indexing and slicing. We can mutate list using by index.

Different methods -   
1. append()  - Add element to end of the list   
2. pop() - remove list element. Default will remove element from end or we can pass the index of item to be removed   
3. sort() - in place sorting for the list. It does not return new list. It will sort the existing list.  
4. reverse() - reverse the list. This is also in place method.   

Use list when objects are order sequence and when we need to get object by index or perform slicing. We can use **sorted(list)** method to sort list which return new list.

## Dictionaries - dict  
Dictionaries are un ordered mapping for storing key-value pairs. This key-value mappings allows user to quickly grab objects without needing to know the index location.  

Dictionaries uses - {"key":"value", "key2":"value2"}

Use dictionaries when we objects are unordered and cannot be sorted.

We can store complex objects in the dictionaries like below

d = {'k1':120, 'k2':[1,2,3], 'k3': {'insideKey': 'Hello'}}

Different methods -
1. keys() - return all keys  
2. values() - return all values  
3. items() - return all key-value pairs  
4. d['key'] - return values associated with key

Dectionaries does not support ordering, but if we like to keep the ordering then we can use - ordereddict

## Tuples - tup  
Tuples are very similar to list, but they are **immutable**. Onces an element is inside tuple, it can not be re-assigned. Tuples uses parenthesis : (1,2,3).

Different methods -   
1. count - Get the count of occurences of input object  

For example - t = ('a','a','b')  .....now t.count('a') --> 2   

2. index - return index of element inside tuple - t.index('b') --> 2  

Tuples mostly used when we pass the objects around the methods, to make sure they dont change.

## Sets - set  
Sets are unordered collections of unique elements. There can be only one representative of the same object.

list = [1,2,1,3,2,4,3,5]
set(list)  --> {1,2,3,4,5}

## Booleans - bool   
Booleans are operators that allow you to convey **true or false**


## Files I/O  
You can open any file in python using below command.

**Reading the file**   

```
myfile = open('myfile.txt')  

myfile.read()  -> Returns entire file --> 'Hello this is a text file\nthis is the second line\nthis is the third line'

myfile.seek(0)  --> Set cursor back to 0 location to read the file again.

myfile.readlines()  --> Read each line and store as list. We can loop throught it and print what is required.

myfile.readline() --> read single line at a time

myfile.close()  --> Close the file


When we do not want to worry about closing the file, we can use **with & as** to open the file like below -  

with open('myfile.txt') as my_new_file:
    contents = my_new_file

```

**Writing to file**   

```
with open('my_new_file.txt',mode='a') as f:
    f.write('\nFOUR ON FOURTH')


with open('my_new_file.txt',mode='r') as f:
    print(f.read())

with open('dkfhdskf.txt',mode='w') as f:
    f.write('My content to the file')

with open('dkfhdskf.txt',mode='r') as f:
    print(f.read())

```

**Different modes**  
r - read only  
w - Write or Overwrite only  
a - append only  
r+ - reading and writing  
w+ - Writing and reading  


## Operators  

**1. Mathematical Operators**  
==, !=, <, >, >=, <=

**2. Logical Operators**  
and, or, not


## Statements and Loops  
Control flow syntax makes use of colons and indentation.

**1. if elif else**  
```
if some_condition:
    #execute some code
elif some_other_condition:
    #do something different
else:
    #do something else
```

**2. For loop**  
Many objects in python are **iterable** such as every element in the list, every character in a string, every key in dictionary.

```
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)
```

When we do not want to use variabl for doing doing . Peopl generally use underscore(_).

**Tuple unpacking**  
Unpack the tuple while iterating over the list  

```
mylist = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in mylist:
    print(a)
    print(b)
```

```
d = {'k1':1, 'k2':2, 'k3':3}

for item in d:
    print(item)

# This will print k1,k2,k3 by default it prints keys. To get key-value, we need to loop through .items()

d = {'k1':1, 'k2':2, 'k3':3}
for key,val in d.items():
    print(val)
```

**3. while loop**   
We can use while to execute some block of code until some condition is True.

```
while some_boolean_condition:
    #execute something
```

We can also combine **else** condition to exeucte if the while condition is not True

```
while some_boolean_condition:
    #do something
else:
    #do something different
```

If we go into continuos loop in  Jupyter, we can use Kernel -> Interrupt or Restart to stop execution.

**4. break, continue, pass**  
We can use break, continue, pass statements in our loops to add additional functionality for various cases.

**break** - Breaks out of current closest enclosing loop.  
**continue** - Goes to the top of the closest enclosing loop.  
**pass** - Does nothing at all.  


**5. Useful Operators**  

**range(10)** - Used in for loop to print numbers upto input number, but not including it.  

```
**Print from 0 to 9**
for num in range(10):
    print(num)

**Print from 3 to 9**
for num in range(3,10):
    print(num)

**Print from 0 to 9 with step size of 2**
for num in range(0,10,2):
    print(num)

list(range(0,11,2)) --> This will create a list with [0,2,4,6,8,10]
```

**enumerations** - We can define a variable and increment it when looping through for/while loop to check how many time we have gone through loop. We can use **enumerate** operator with tuple unpacking like below.

```
word = 'abcde'

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')
```

**zip** - Zip content of 2 or more list into one for iterate over it. If list or uneven, then it will zip with small length list. It will ignore everything which is extra.

```
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for item in zip(mylist1,mylist2,mylist3):
    print(item)

This will print 

(1, 'a', 100)
(2, 'b', 200)
(3, 'c', 300)


list(zip(mylist1,mylist2,mylist3)) --> [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]

```

**in** - This operator checks if the element is in the list. Return True/False. It works with list, string, dictionaries.

```
'x' in [1,2,3] --> False

'x' in ['x','y','z'] --> True

'o' in 'a world' --> True

'mykey' in {'mykey':345}  --> True

d = {'mykey':345}
345 in d.values()  --> True
```

**min/max** - Get the min and max

```
mylist = [10,20,30,40,50,100]
min(mylist) --> 10
max(mylist) --> 100
```

**random** - Python comes with a lot of different libraries. We can import random library and use a lot of function inside that library.  

shuffle - Shuffle elements in place

```
#Shuffle mylist
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)

#Random integer from 0 to 100
from random import randint
randint(0,100)

```

**input** - Ask user for input. We can pass optional text message to show to user. Input parses anything passed to it as String.

```
result = input('Enter a number here:')
result --> '20'

type(result) --> str
float(result) --> 20.0
int(result) --> 20

#OR we could do below to get number in proper format
result = int(input('Whats your favorite number?'))
```

**6. List Comprehensions**  
List comprehensions are unique way of quickly creating list with python.  

We have below code to convert string into list of characters.
```
mystring = 'hello'
mylist = []

for letter in mystring:
    mylist.append(letter)
mylist --> ['h','e','l','l','0']
```
We can use list comprehension to reduce the line of code and write this in one line with below code -
```
mylist = [letter for letter in mystring]
mylist --> ['h','e','l','l','0']

mylist = [x for x in 'word']
mylist --> ['w', 'o', 'r', 'd']

mylist = [num for num in range(0,11)]
mylist --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Square of each element in array
mylist = [num**2 for num in range(0,11)]
mylist --> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Print even number
mylist = [x for x in range(0,11) if x%2==0]
mylist --> [0, 2, 4, 6, 8, 10]

#Complex
celcius = [0,10,20,34.5]
fahrenheit = [(9/5)*temp + 32 for temp in celcius]
fahrenheit --> [32.0, 50.0, 68.0, 94.1]

#More complex with if else - We should not write like below, it's not readable, but possible
result = [x if x%2==0 else 'ODD' for x in range(0,11)]
result --> [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]

#Nested loops
mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
mylist --> [200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

#With comprehension
mylist = [x*y for x in [2,4,6] for y in [100,200,300]]
mylist --> [200, 400, 600, 400, 800, 1200, 600, 1200, 1800]
```

**7. Join**  
Join is used to join the list with specified pattern.

```
'--'.join([a,b,c])  --> 'a--b--c'
' '.join(['Hello','World']) --> 'Hello World'
```

## Methods and Functions  

**1. Methods**  
Built in objects in Python have variety of methods we can use. In Jupyter notebook, we can use SHIFT+TAB to get help for the method signature and details about them.

We can also use help function to get the help like -
```
help(mylist.insert) --> This will return help about the insert function.
```

**2. Functions**  
Functions allows modularity in the programming.

```
#Basic function
def name_of_function():
    #Explain function
    print("Hello")

#Function with arguments
def name_of_function(name):
    #Explain function
    print(f'Hello {name}')

#Function returning value
def add_function(num1, num2):
    return num1 + num2

#Function with documentation - We can do SHIFT+TAB to get the help and it will show below doc from **'''Help'''**
def add_function(num1,num2):
    '''
    DOCSTRING:This can be used to add 2 numbers
    INPUT: 2 numbers, num1 & num2
    OUTPUT: Result output will be addition of 2 input numbers
    '''
    return num1 + num2

#Default argument, when not passed from caller of the program.
def say_hello(name='NAME'):
    print('hello '+name)
say_hello('Vaibhav') --> hello Vaibhav
say_hello() --> hello NAME

#PIG_LATIN word
def pig_latin(word):
    first_letter = word[0]
    #Check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word
```

**3. \*args and \*\*kwargs**
These are 2 functional parameters - argument and keyword argument. These are used for getting arbitary number of arguments and keyword arguments.

```
def myfunc(*args):
    return sum(args) * 0.05
myfunc(40,60)
myfunc(40,60,100,1)
```
**\*args are treated as tuple** inside the function, so if we print args inside a function, it will print the tuple containing all the input arguments. Arbitary argument name can be anything, but we need to put * in front of to make if accept arbitary number of arguments.

**\*\*kwrgs are treated as dictionaries** inside the function.

```
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple') --> My fruit of choice is apple
myfunc(fruit='apple',veggie='lettuce') --> It will work without any issues
```

We could use *args & **kwargs both in same function as below -

```
def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')

--> Output is
(10, 20, 30)
{'fruit': 'orange', 'food': 'eggs', 'animal': 'dog'}
I would like 10 eggs
```

**4. Lambda Expressions Map an Filter**  

**map**  
Map data from input iterable to output by applying a passed function on each element in the iterable
Just pass the function name and iterable to map.

```
# Syntax
map(func, iterable)

def square(num):
    return num**2

# Print square of the array elements
for item in map(square,[1,2,3,4,5]):
    print(item)

# Same as above
list(map(square, mynums))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy','Eve','Sally']
list(map(splicer, names))  --> ['EVEN', 'E', 'S']
```

**filter**  
Filters the data from the iterable based on the passed function and return new filtered iterable.

```
# Syntax
filter(func, iterable)

def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]
list(filter(check_even,mynums))  --> [2, 4, 6]
```

**Lambda expressions**  
Complex operations can be written in simple way using map, filter and lambda expressions. Lambda expressions are annonymous functions that can be used only once.

```
# Normal function
def square(num):
    return num**2

# Converted lambda expression - We have to make use of labmda keyword
square = lambda num: num**2

square(4)  --> 16

# We dont need to assign the name to lambda expression, most of the time we will use them as anonymous function like below -

list(map(lambda num:num**2, mynums))  --> Map input to output with square
list(filter(lambda num:num%2==0, mynums))  --> Filter even numbers
```

We should create lambda function only when they are easy to read and are small.

**5. Nested statements and scope**  
When we create a variable in python, it is store in the namespace and has associated scope with it. Scope decides the visibility of the variable to other parts of the code.

Python follows LEGB rules format for scoping -

L - Local
E - Enclosing functions local
G - Global
B - Built it like open, range, list

Python will look for variable from Local to Built in, if not found will throw an error.

```
# GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():
    
    # ENCLOSING
    name = 'Sammy'
    
    def hello():
        # LOCAL
        name = 'I AM LOCAL'
        print('Hello '+name)
    
    hello()

greet()  --> Hello I AM LOCAL
```

We can use **global** keyward to grab or reassign the global variable to some different values, but we should avoid it.

## Object Oriented Programming  

OOP allows programmers to create own custom objects with state and methods. We can encapsulate the code using classes and create methods inside it. __init__() is a special method inside every class which helps us to instantiate the object.

Class is a blueprint from which we can create many objects.
```
class NameOfClass():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        print(self.param)

# Define a class
class Sample():
    pass

# Create instance of class
my_sample = Sample()

type(my_sample) --> __main__.Sample
```

**1. Attributes**  

**instance attribute** - Instance attributes are definded at the time of creation of the instance using self keyword in the __init__ method.  

**class attributes** - Class attributes will be same for any instance of the class. They are class level rather than instance level. We don't need self keyword for this as self keyword is used when we need to define for instance of the class.

```
class Dog():
    
    # CLASS OBJECT ATTRIBUTE
    # THESE WILL BE SAME FOR ANY INSTANCE OF CLASS
    species = 'mammal'
    
    def __init__(self,breed,name,spots):
        
        # Attribute
        # We take in the argument
        # Assign it using self.attribute_name
        
        self.breed = breed
        self.name = name
        self.spots = spots
```

To refer the class attributes, we can use **self. as well as ClasName.** For example -  

```
self.species --> mammal
Dog.species --> mammal
```

**2. Methods**
Methods are functions which are defined inside the class to work with the class attribute or provide extra functionality to the classes. To refer the instance attribute in the class, we need to use self. For passed arguments to methods, we can directly refer them by name.

```
def bark(self,number):
    print("WOOF! My name is {} and the number is {}".format(self.name,number))


class Circle():
    
    # CLASS OBJECT ATTRIBUTE - 
    pi = 3.14
    
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
        
    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2

# Create an instance
my_circle = Circle(30)

my_circle.get_circumference()  --> 188.4
my_circle.area --> 2826.0
```

**3. Inheritance**
Inheritance helps us to define parent child relationship between classes to reuse the methods definded by the parent class

```
class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
        
    def who_am_i(self):
        print("I am an animal")
        
    def eat(self):
        print("I am eating")


class Dog(Animal):
    
    def __init__(self):
        # INSTANTIATE ANIMAL OBJECT
        Animal.__init__(self)
        print("Dog Created")
    
    # OVERRIDE THE METHOD FROM ANIMAL CLASS
    def who_am_i(self):
        print("I am a Dog")
      
    # ADD NEW METHODS TO CHILD CLASS
    def bark(self):
        print("WOOF!")

my_dog = Dog()
>> ANIMAL CREATED
Dog Created

my_dog.who_am_i() --> I am a Dog

my_dog.eat() --> I am eating

my_dog.bark() --> WOOF!
```

**4. Polymorphism**  
Same name with different forms. We have 2 Class below Dog and Cat which has speak() method and another print_pet method which calls the speak method of the pet, so print_pet dont know what will be input object. print_pet will react different based on the input object we will pass, this is called as polymorphism.

```
class Dog():
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + ' says woof!'

class Cat():
    
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + ' says meow!'


def print_pet(pet):
    print(pet.speak())

niko = Dog("niko")
felix = Cat("felix")

print_pet(niko) --> niko says woof!
print_pet(felix) --> felix says meow!
```

**5. Abstract classes**  
Classes which expects never needs to be instantiated. It is designed to seve only as a base class.

```
class Animal():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

my_animal = Animal('Frankie')
my_animal.speak() --> This will throw an error that this class needs to be implemented by another child class

class Dog(Animal):
    
    def speak(self):
        return self.name + ' says woof!'

class Cat(Animal):
    
    def speak(self):
        return self.name + ' says meow!'

fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak()) --> Fido says woof!
print(isis.speak()) --> Isis says meow!
```

**6. Special(Magic/Dunder) method**  
We can use paython build in methods and functions to enhance the class to give more information about the class or add more functionality on the class.

If we create object and print it. It will print the location of object in the memory, but we can also use str method print nice pretty output.

__init__  --> This is special method which helps us create an instance of the object
__str__ --> Helps us to write the string representation of the object
__len__ --> print the lenght
__del__ --> to delete the object and do some more functionality

```
class Book():
    
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"This is {self.name} book by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print(f"The book {self.name} is deleted successfully")

```

## Modules and Packages  
PyPI is a repository for open source third party python packages. To install these third party libraries, we can use **pip install**.

We can also create our own packages and module -

**1. Modules**  
Modules are just .py scripts that you call in another .py script

```
mymodule.py

def my_func():
    print("Hey I am a in mymodule.py")

myprogram.py

from mymodule import my_func
my_func()

#When we run python myprogram.py, then we get output as "Hey I am in my mymodule.py"
```

**2. Packages**  
Packages are collection of modules. We need to create a package folder and create __init__.py file inside each package directory, so that python understands that these are not just folders, but packages. Place the .py file inside the package folder and them use them in the program.

**3. __name__ and "__main__"**  
There is not main() function in python, so how do we know which code to execute first. When we submit the python file.py command to python interpreter, it will execute all the first level statements which will  register all the classes and methods and functions in python. Python also assigns a value to a built in variable __name__, so we we run the program, it assigns values as __name__ = "__main__".

We can use the value of __name__ to check if the main file is being run or imported in the another python module.

```
def my_function():
    print("This is my function")

def add():
    print("This function is used for addition")

# RUN THE FUNCTIONS IN MAIN
if __name__ == '__main__':
    my_function()
    add()
```

## Errors and Exception Handling  
We use 3 keywords for this

**try:** This is the block of code to be attempted(may lead to an error)  
**except:** This block of code will get executed if there is any error in try block  
**finally:**  A final block of code to be executed regardless of an error  

```
# More general error
try:
    f = open('testfile','r')
    f.write("Wite a test line")
except:
    print("There was a type Error!")
finally:
    print("I always run")

# Catch specific errors and show appropriate error messages
try:
    f = open('testfile','w')
    f.write("Wite a test line")
except TypeError:
    print("There was a type Error!")
except OSError:
    print("Hey you have an OS Error")
finally:
    print("I always run")

# try/except/finally inside a function
def ask_for_int():
    try:
        result = int(input("Please provide a number"))
    except:
        print("Whoops! That is not a number")
    finally:
        print("End of try/except/finally")

# Go in loop till we get number
def ask_for_int():
    
    while True:
        try:
            result = int(input("Please provide a number"))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")

```

## Pylint and Unit Testing  
As we begin to write code and have large number of modules, then we need to have unit test code which will execute to make sure we are not breaking old code while writing a new code.

There are 2 libraries in python which helps us to achieve this -

**1. pylint** - This library looks at code and reports back possible issues like syntax error, formatting issues and styling etc  
**2. unittest** - This built in library allow you to test your own programs and check you are getting desired outputs

Python has set of styling convention rules known as **"PEP 8"**.

Install pylink library using -  
```
pip install pylint
```

We can run pylink using -

```
pylint simple1.py
```

This will print all the statistics of the code including possible styling and syntax issues.




































## Problems link for exercise

- Basic Practice - http://codingbat.com/python  

- More Mathematical (and Harder) Practice - https://projecteuler.net/archives  

- List of Practice Problems - http://www.codeabbey.com/index/task_list  

- A SubReddit Devoted to Daily Practice Problems - https://www.reddit.com/r/dailyprogrammer  

- A very tricky website with very few hints and touch problems (Not for beginners but still interesting)- http://www.pythonchallenge.com/  

