# Youtube link : https://www.youtube.com/watch?v=VchuKL44s6E&list=WL&index=115&t=3456s&ab_channel=TechWithTim 
# for code visualisation: https://pythontutor.com 

#DATA STRUCTURE

# Arrays which is also called lists in python is most commonly used data structure.  eg: arr = [1, 2, 3]. , list = [1, "Sujan" , "True"]

# Lists store items that are of various data types. This means that a list can contain integers, floating point numbers, strings, or any other Python data type, at the same time.
# That is not the case with Arrays.  Arrays store only items that are of the same single data type. 
# There are Arrays that contain only integers, or only floating point numbers, or only any other Python data type you want to use. eg: arr = [1, 2, 3]. , list = [1, "Sujan" , "True"]

# Hashmap (aka dict)
# Hash maps are a common data structure used to store key-value pairs for efficient retrieval. A value stored in a hash map is retrieved using the key under which it was stored.
# it is commonly referred to as a dictionary (dict). A dictionary is a collection of key-value pairs, where each key must be unique. eg: my_dict = {'name': 'John', 'age': 30, 'city': 'New Yor k'}

# Tuples. Its similar to lists/arrays and assigned with normal brackets but are immutable meaning cannot be changed 
# i.e. it cannot be removed or cannot be appended which is why its can be called immutable lists. eg: tup = (1, 2, 3)

# Sets datatype. sets is basically unordered unuque collection of elements. We can use sets when we care to check if something exists or doesnt exists
#example of creating a set and adding different datatypes to it
#sets will not contain duplicate elements meaning if we try to add something same lets say integer the second time it will only count the first. 
# eg:
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)                      # show that duplicates have been removed
# {'orange', 'banana', 'pear', 'apple'}


#DATA TYPES

# Integer is any whole numbers
#533543545 # -65451

# Float is any number with decimal 
# achba.0 # -5.3

#String is anything surrounding by single or double quotes
# "hello"  #'hello' #Even numbers if included inside quotes are string for example "-4.6" is string not float

#Boolean
#It is one of 2 values. We have True or False value 


#user input
#we just use input function and it has to be inside stringfor example 
# input("Job Title: ")
#and to get the input value and store what the user typed in so we can use it later we need to assign the input to variable for example
# Position = input("Job Title: ")
# print("Hello Sujan your position is ", Position, "Good luck")

#Arithmetic operators (mathematical operations)
#Example 1
# a = 5.5
# b = 3.5
# result = a + b
# print(result)

#Example 2
# x = 25
# y = 5
# result = (x % y) * 2
# print(result) #Result is 0 because 5 * 5 = 25 and remainder is 0 whcih is multiplied by 2

#Example 3.1 with input
#num = input("Number: ")
#print(int(num) - 5) #Extra int has been added to print func because in the previous line whatever we put as input for number it will be considered as string i.e. num value will be considered as string so to make sure num is considered as numeric value we added int inside print function.
#so basically the int inside print func will convert "5" to 5 which is real integer

#Example 3.2 with input but using float instead of int so we get result in decimal
# num = input("Number: ")
# print(float(num) - 5) 

#string method
# hello = "hello"
# print(type(hello)) #type wil show the type of variable. So basically it will print class/datatype called string
#now string method is something with dot operator for example lets take  .upper() string method. There are so many methods like .count , .lower etc
# hello = "hello".upper() 
# print(hello) #it will print the variable for hello in upper case

#we can also use as below
# hello = "hello"
# print(hello.upper()) #its the same result as above


#Conditional operators will basically return us boolean value after comparision i.e. True or False (core conditional operators are == , != , >= , <= , > , <) 
# x = "hello"
# y = "hello"
# print(x == y) # to check comparison (here it will return true)

#chained conditionals more properly called as comppound conditions which basically means commbining multiple conditions together to get 1 large condition.  Chained conditionals would be x < y < z.
# bascally to combile we can use: and , or , not 
# x = 7
# y = 8
# z = 0

# result1 = x == y
# result2 = y > x
# result3 = z < x + 2 

# result4 = result1 or result2 or result3
# print(result4)

#Conditional statements (elif should be after if statement and before else statement. elif can be as many times as we want but it cannot be after else statement). We can also just use if and elif without else which is totally valid.
# x = input("position: ")

# if x == "DevOps":
#     print("Wow, you are in good path. Good luck!")
# elif x == "Software Engineer":
#     print("Nice one mate")
# else:
#     print("Maybe you should try considering something else bruv")

#collections (collection is simply an unordered or ordered group of elements for example lists and tuples). Elements ate simply some data type.
#lists. Lists is an ordered collection and many different data types can be added so basically it can store a bunch of different elements. Lists are mutable and they can be changed. 

#Example 1
# x = [7 , "hello", False ]
# print(x)

#Example 2. Appending things to the list
# x = [7 , "hello", False ]
# x.append("wtf bruv") #This append will basically add this value to the above list
#print(x)

#Example 3. Using extend
# x = [7 , "hello", False ]
# x.extend([4,5,6,7]) #This extend will basically extend the values to the above list. It can be used when multiple things can be extended
# print(x)

#tuples. Its similar to lists and assigned with normal brackets but are immutable meaning cannot be changed i.e. it cannot be removed or cannot be appended which is why its can be called immutable lists.
#Example 1
#x = (7 , "hello", False )
#x.append("wtf bruv") #This append will basically add this value to the above list  but as we are using tuple object here it will fail with an error
#print(x[0])

#for loops
#Example 1.lets print the number from 1-10
#for i in range(10): #range is a function here and the number we put inside will make sure it range will go upto 10 not till 10 and not include 10.We can include more numbers inside
#   print(i)

#example 2 with more numbers inside range function
# for i in range(10,-1,-1):
#     print(i)

#Looping through lists. There are 2 ways we can loop throught lists
#Example 3.1
#for i in [2,4,6,8]:  #so instead of range we simply put the list
#    print(i)  # so this will print all of the numbers inside the lists

#Example 3.2. The other way is simply calling the list variable in loop.
# x = [2,4,6,8]
# for i in x:
#     print(i)

#while loops
# i = 3
# while i < 5:
#     print("makes sense")
#     i += 1

#we can write the same above code like below for while loop by implementing break statement
# i = 3
# while True:
#     print("makes sense")
#     i += 1
#     if i == 5:
#         break   #This will simply break the closest loop above

#slice operator. What slice operator does is it essentially allows us to take a slice of a collection like string or a list or a tuple etc and do something with it.
# the operator is simply the square backet with sequence of colon in it i.e. sliced = [::] meaning sliced = [start:stop:step]
#example 1.1
# x = [0,1,2,3,4,5,6,7]

# sliced = x[:4]  # so we are putting 4 after first colon meaning it should iterate upto four numbers from the list and stop as we put index inside sliced as 4.
#print(sliced)

# #example 1.2
# x = [0,1,2,3,4,5,6,7]

# sliced = x[2:]  #this is saying start at 2 and finish at the end of the above list.
#print(sliced)

#example 1.3
# x = [0,1,2,3,4,5,6,7]

# sliced = x[2:4] #start from number 2 of the above varible and stop at the fourth number
#print(sliced)

#example 2 with string
# s = "DevOps"

# slice = s[:4]  #can be slice or sliced doesnt matter
#print(slice)

#sets datatype. sets is basically unordered unuque collection of elements. We can use sets when we care to check if something exists or doesnt exists
#example of creating a set and adding different datatypes to it
#sets will not contain duplicate elements meaning if we try to add something same lets say integer the second time it will only count the first
# x = set()  # we just created an empty set called x 
# x.add(55) # added integer 55
# x.add(45) #added second integer for an exampple but this will not be considered
# x.add(False) #added boolean vaiue False
# x.add(4.555) #added number as a Float
# x.add("Jetski") #added string
# print(x) #will print everythig we have added to the set. Each item inside a set is called element. Elements will1 printed in different order but it doesnt matter for sets. sets differs from lists and tuples where order matters

#to remove we simple need to use x.remove
# x.remove(False)
# print(x) #now it will print without boolean value

#Dictionaries. It is basically a key value pair i.e. x = {"key":"value"}. The value could be a single value or even a list
#example 1
# x = {"key":"777"}
# print(x["key"]) # to print the value of the key


#example 2 adding more dicts to existing ones
# x = {"key":"777"}
# x["key2"] = 666 #so here we are adding new dict. These keys can be of different data types like strings,integers etc
# print(x)

#finally in order to veryfy if something is in the dictionary then we can test as below
# x = {"key":"777"}
# print("key" in x)

#to loop over a dict example
# x = {"poda":"777"}

# for poda, value in x.items():
#     print(poda,value)

#Functions i.e. starts using def keyword
#Example 1
# def func():   # here func is the function name is the same as variable name and inside brackets we can put paramater/arguments or leave it empty
#     print("Don")

# func()      #If we dont call like this at the end then the function wont run

#Example 2 defining function inside a function

# def func():   
#     print("Don")
#     def func2():
#         print("Musa")
#     func2()  #Notice that in this advanced example 2 I have to end it like this for defining functtion inside a function

# func()

#Example 3 defining function with arguments(inside brackets)

# def func(x, y):   # Step 1: so here x and y arguments were added
#     print("Don", x, y) #Step 2: Final add the same args here in order to print them

# func(7, 8)  # Step 3: When you add arguments above you need to value for x and y

#Example 4 defining function with arguments and returning something from the function

# def func(x, y):   
#     print("Don", x, y)
#     return x * y #Just multipying the values added to tehse args. We can also return multiple values.

# print(func(7, 8))  # so now this will print the functiona and also return the multiplication value above


# Unpacked Operetor , *args and **kwargs(key word arguments). key word args looks like one=0, two=3 etc
#Unpacked operator it separates all the elements from the lists into individual elements
#Example 1 of unpacked operator

# x = [1, 23, 6544, 8794653 ]
# print(*x) # here *x is the unpacked x  so it will take the whole list, separate them and pass them into and arguments unlike print(x) whcih will print in a single list. Double asterisk is used for dicts and single asterisk is for lists & tuples.

#Example 2 *args and *kwargs. These are usefull when we are not sure how many arguments we need to put inside a function. so what *args  & **kwargs will do it it will allow us to pass an unlimited amount of regular arguments or key word arguments

# def func(*args, **kwargs):
#     print(args, kwargs)

# func(9,8,7, one=5, two=10) # so the result of args will be tuple with printing positional arguments like 9,8,7 and kwargs will print key word arguments

#Scope and Global
#Example 1
# x = "Esjay"

# def func(name):
#     x = name  #in this line the variable will not be changed for x from Esjay to name with func changed in line 259 because this lines x variable is local within the scope of this function but the x variable in line 253 is global and not defined within scope

# print(x)
# func("changed")
# print(x)

#Example 2 with global where func changes because of line 269
# x = "Esjay"

# def func(name):
#     global x
#     x = name
  
# print(x)
# func("changed")
# print(x)

#Raise an Exception in python
#this is basically to throw an error creared by us to make an exception
#example 1
# raise Exception("wtf are you doing bruv?")

# #example 2
# raise FileExistsError("Yo this file doesnt exist") #String is the actual message we will see with the error we raised

#Handling Exceptions using try, except and finally block
# try:  #meaning try whatever is inside this try block
#     x = 7 / 0 #we know that this going to cause error
# except Exception as e:  #whatever is the exception will be stored in variable e. If this exceot block was not there then we would get an error with try block
#     print(e)
# finally:
#     print("finally its done") # clean up type operation is under finally block meaning no matter what exception rises earlier we are going to close this whole block with finally
    

#Lambda
#Lambda is an one line anonymous function meaning which means we dont define a lamda with def as we do to create other functions.
#Example 1

# x = lambda x: x + 10
# print(x(3))   #basically 10 will be added with 3 as the parameter for x is given as 3 here

# #Example 2
# x = lambda x, y: x + y
# print(x(10, 20)) #will just add 10 + 20. Just remember we are printing x as we set it as lambda in previous line

# Map and Filter (lambda is usefull here but not mandatory)
# Example 1 with map
# x = [1,2,5,8,9,7,3] 
# #below we will create a map.What map will do is take all the elements of the list from above and use a new function to map them into a new lists. So basically we can use func like lambda or anything else inside a map
# mp = map(lambda i: i + 2, x) #we are going to map all of the elements inside the x var to the lambda function i.e. (lambda i: i + 2). Basically take this lambda function and add it to every single element of x var then out them into new list.
# print(list(mp)) #to print in list representation of mp. We can also use tuple instead of list.

#Example 1 with filter with lambda
# x = [1,2,5,8,9,7,3] 
# mp = filter(lambda i: i % 2 == 0, x) # here basically this labmda function i.e. (lambda i: i % 2 == 0)  has to return true/false based on the value of items basically only print the value if its even. 
# print(list(mp)) 

#Example 2 with filter without using lambda but creating new function
# x = [1,2,5,8,9,7,3] 

# def func(i):
#     i = i * 3
#     return i % 2 == 0 #basically created similar to lambda

# mp = filter(func, x) #replacing func with lambda as we created our own similar func like lambda
# print(list(mp)) 

# F string (only available from pyton 3.6). Lower case f or capital case F it doesnt matter.
# z = "Nasoor"
# x = f"hello {z} what is {2 + 2} + {2+3}?"  # if we wanna embed an expression we can use it with curly braces. We can also adapt another variable same way
# print(x)

# list compprehention in 2 different ways to get same output
# arr = [i for i in range(7)]
# print (arr)

# i = []
# for x in range(7):
#     i.append(x)
# print(i)
