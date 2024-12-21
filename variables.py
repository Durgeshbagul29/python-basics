'''Variable is a container which stored some data types values.
No need to declared data type with variable name and no need add semicolon in python to end of statment,in naming canvensions python prefred snake_case '''

# We can use # [single line] and ''' [multiple lines of code] to comment any line of code in python 


# String = collections of char, declared in single qoute or double qoute
name = "Durgesh"

# Int = number which positive or negative
age = 18

# Float = decimal values which is pointing 
percentage = 85.9

# Complex = which is stored complex values [sub type of number data tyepe]
complex = 1+2j

# Boolean = True or False 
is_Student = True

# List = sequence of same data types declared in [] bracket, list is mutable = we can also change after declartion 
stud_list = ["Durgesh","Gaurav","Vrushali"]
print("List ->", stud_list)

# Tuple = collections of multiple elements, declared in () paranthesis, tuple is inmutable = It means one's we declared can't change it 
numbers = (1,4,6,3,7)
print("Tuple ->",numbers)

# Dictonary = we can stored data by using key-values pairs, declared in {} caraly bracket
item = {
    "name" : "Paper",
    "price" : "20 RS"
}
print("Dictonary ->",item)

# Set = collections of all unqiue elements, declared in {} caraly bracket
fruits = {"Apple","Banana","Grapes"}
print("Set ->",fruits)

# None = which is stored null values
# type() = used this function for check data type of a variable 
raj = None
print(type(raj))

# end="" => We can add next print statement end of current statement
print("Hello", end="")
print("Coders.")

# We can use comma for concatination with diffrent data types. 
print("My name is", name ,"and my age is", age, "and my percentage is",percentage)

# We can separate variables by sep=" " function as passed argument
print(name,age,percentage,is_Student, sep=":")

# We can denifed multiple variables in single line by using semicolon
a = 1; b = 2; c = 3; d = 4
print(a,b,c,d, sep="->")
