# Operators and it's tyeps

# Arithmetic Operators
'''
Addition (+) -> to add two or more numbers and also used for String concatination
Subtraction (-) -> to subtract values into another value
Multiplication (*) -> to multiply some numbers and returns product of given numbers
Division (/) -> to divide number and return 
Floor Dividion (//) -> It returns nearest whole number 
Modulus (%) -> to returns reminder of given numbers
Exponentiation (**) -> to returns power of given numbers
'''

# Examples :- 
print("Addition:", 3 + 5)
print("Subtraction:", 5 - 4)
print("Multiplication:", 3 * 5)
print("Division:", 15 / 4)
print("Floor Division:", 15 // 4)
print("Modulus:", 10 % 2)
print("Exponentiation(square):", 10 ** 2)
print("Exponentiation(cube):", 2 ** 3)


# Assignment operators
'''
= equal :- to assign right value in left variable or element
+= :- to addition, same as left value num1 = num1 + num2
-= :- to subtract, same as left value num1 = num1 - num2
*= :- to multiply, same as left value num1 = num1 * num2
/= :- to divide, same as left value num1 = num1 / num2
%= :- to modulus, same as left value num1 = num1 % num2
//= :- to floor division, same as left value num1 = num1 % num2
'''

# Comparison Operators
'''
== Double equal to :- to compare two values or elements, it's ans always in true and false
!= Not equal to :- opposite of double equal to and compare to two values or elements
> Greater than :- to check left value is big than right value
< Less than :- to check left value is small than right value
>= Greater than equals to :- to check left value is big or equal to right value
<= Less than equals to :- to check left value is small or equal to right value
All return it's values in true or false format
'''

# Logical Operators
'''
We can used logical operators by combining two conditions
&& and Returns true if both elements are true
|| or  Returns true if one of the element is true
~ NOT  Returns reverse result of the given element
'''

# Identity Operators
'''
is -> Return true if the both variable are the same object
is not -> Return true if the both variables are not the same object
'''
a = 5
b = 5
print("Same", a is b)
print("Not Same", a is not b)

# Membership Operators
'''
in -> Returns True if a given values present in a sequence
not in -> Returns True if a given values not present in a sequence
'''
list = [1,2,3,4,5]
print("present:", 6 in list)
print("Not Present:", 6 not in list)


# Bitwise Operators
'''
Computers only understand binary number system which only form in 0 and 1.
0 - 9 is the decimal number system.
Que :- How to convert demical number into binary values
Ans :- Divide by 2 of given number and write down to up format, there only two reminder 0 or 1.
      22 =  0   \   22
            1   \   11
            1   \   5
            0   \   2
                \   1     = 10110

Que :- Hoe to convert binary number into decimal numbers
Ans :- Gives first digit and product into 2 of remaining digits, addition of all values.
      10110 -> (1 * 2**4) + (0 * 2**3) + (1 * 2**2) + (1 * 2**1) + (0 * 2**0) = 22
      
      1 - > True, 0 -> False
      & AND -> if both are same then returns true
      \ OR -> if one is 

'''

# Operators Precedence :- used BODMAS () / * + - Rule
# Another oparators :- (), **, / // %, *, + -, >> << bitwise, & \ ^ , comparison == != => <= > < , logical and or  