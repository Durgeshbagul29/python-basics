''' Tyepecasting :- 
For another data tyeps we can used type casting here It means converting one data type into another data type  
'''
num = 12
print(float(num))

# String => 235   Covert interger into String
a = 2; b = 3; c = 5
a_str = str(a)
b_str = str(b)
c_str = str(c)
final_str = a_str + b_str + c_str
print(final_str)


# input() -> by using this function we can get input from user, but this functon always captured as String input 
user_name = input("Enter your name: ")

# print() -> by using this function we can print on the console
print(user_name)

# For integer
age = int(input("Enter your age: "))
#print(type(age))
print(age)

# For float
percentage = float(input("Enter your percentage: "))
#print(type(age))
print(percentage)