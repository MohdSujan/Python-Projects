#code challenge
# two_digit_number = input("Type a 2 digit num: ")

# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])

# result = first_digit + second_digit
# print(result)


#code challenge
# height = input("enter your height in m: ")
# weight = input("enter yoru weight in kg: ")

# bmi = int(weight)/float(height) ** 2
# print(bmi)
# bmi_as_int = int(bmi) #to print as whole number
# print(bmi_as_int)

#an example of using f-string
# score = 0
# fat = 46.2
# print(f"your score is {score}, your fat percentage is {fat}%")

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip are you goin to give? 10,12 or 15? "))
people = int(input("How many people are going to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)