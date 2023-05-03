#functions with outputs using return

# def format_name(f_name, l_name):
#     formatted_fname = f_name.title()
#     formatted_lname = l_name.title()
#     return f"{formatted_fname} {formatted_lname}" #using return here instead of print(f"{formatted_fname} {formatted_lname}") to get an output
    
# output_of_return = format_name('sujaN','DON') #while calling the function with arguments we need to save it in a variable in order to print in console
# print(output_of_return) 
# #OR
# print(format_name('sujaN','DON')) #alternative

#functions with outputs using multiple returns

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didnt input anything" #this is to make sure that if there are no inputs then  prevent the rest of the code from being executed.
#     formatted_fname = f_name.title()
#     formatted_lname = l_name.title()
#     return f"{formatted_fname} {formatted_lname}" #using return here instead of print(f"{formatted_fname} {formatted_lname}") to get an output
    
# print(format_name(input("What is your first name?"), input("What is your last name?")))

#code challenge 1. days in month
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(inputed_year, inputed_month):
#     if month > 12 or month < 1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#     if is_leap(inputed_year) and inputed_month == 2:
#         return 29
#     else:
#         return month_days[inputed_month - 1] # the -1 is added incase the inputted month is Jan as the index in list starts from 0
        
        
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

#final calculator project
from art import logo

def  add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def divide(n1, n2):
  return n1 / n2

def multiply(n1, n2):
  return n1 * n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
 }

def calculator():
  print(logo)
  num1 =  float(input("What is your first number? ")) #added float instead of int because we can expect decimal numbers to be calculated. whole numbers are also fine with float datatype.

  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number? "))
    calculation_function = operations[operation_symbol] #creating a calculation_function function to tap in dictionary and get the symbol 
    answer = calculation_function(num1, num2) #inputs are num1 and num2

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator() #this method is called recursion i.e. calling own function 
                   # so When the user will type "n" then everything will start from the beginning like new calculation with new num1 and num2
  
calculator()