# We can follow Indentations rules in python It means spacing of a particular block of code. If we are not following then it will be throws indentation error.

# Conditionals Statements :-

# If - Else 
is_raining = True
if is_raining:
  print("Take Umbrella")
else:
  print("Don't  Tacke Umbrella")
  
  
# If - Elif - Else
num = 0
if num > 0:
  print("Number is Positive.")
elif num == 0:
  print("Number is Zero")
else:
  print("Number is Negative.")
  

# Neasted If - Else   => Inner if-else statments
num1 = int(input("Enter your number 1: "))
num2 = int(input("Enter your number 1: "))
num3 = int(input("Enter your number 1: "))
if num1 > num2:
  if num1 > num3:
    print(num3, "is bigger than other numbers")
elif num2 > num1:
  if num2 > num3:
    print(num2, "is bigger than other numbers")
elif num3 > num1:
  if num3 > num2:
    print(num3, "is bigger than other numbers")
elif num1 == num2: 
  print("num1:", num1, "and numb2:", num2, "is both are equals")
elif num2 == num3:
  print("num2:", num2, "and numb3:", num3, "is both are equals")
else:
  print("num1:", num1, "and numb3:", num3, "is both are equals")
  
  
# Match Case : It same as Switch Case, used _ uderscore for deafult statment in here.
number1 = float(input("Number 1: "))
number2 = float(input("Number 2: "))

opeartion = input("Enter operator { + - * / }: ")

match opeartion:
  case "+":
    print(number1 + number2)
  case "-":
    print(number1 + number2)
  case "*":
    print(number1 - number2)
  case "/":
    print(number1 / number2)
  case _ :
    print("Enter valid opeartion.")
    

# Ternary Operator :-
'''
Synatx :-  variable = "first statment" if condition else "second statment"
''' 
number = int(input("Number: "))
result = "Number is even" if number % 2 == 0 else "Number is odd"
print(result)

# We can used in single line also
print("Result:", "Number is even" if number % 2 == 0 else "Number is odd")


# Loops :- 
'''
For Loop :- syntax => for i (_) in range (i start (optional default 0), condition, steps (optional))
'''
# value = int(input("enter value: "))
for i in range (1, 11):
  print(i, "Hello")
  
# without using i it means any types received
for _ in range (1, 11):
  print("Ram")

# Add one more state as step
for i in range (1, 11, 3):
  print(i, "Durgesh")
  