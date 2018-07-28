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

## Strings  
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


## Lists
Lists are order sequences that can hold variety of object types. They use brackets[] and commas to separate objects in the list, [1,2,3,4]. List supports **indexing and slicing**.

They are similar to Strings like we can contact 2 list using + operator, can do indexing and slicing. We can mutate list using by index.

Different methods -   
1. append()  - Add element to end of the list   
2. pop() - remove list element. Default will remove element from end or we can pass the index of item to be removed   
3. sort() - in place sorting for the list. It does not return new list. It will sort the existing list.  
4. reverse() - reverse the list. This is also in place method.   


## Dictionaries  

