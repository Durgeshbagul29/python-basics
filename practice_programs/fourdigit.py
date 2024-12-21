# WAP to check given number int this present four digit or not

number = int(input("Enter your number: "))

if (number >= 1000 and number <= 9999) or number == 0000:
  print("Your number is four digit.")
else:
  print("Your number is not four digit")