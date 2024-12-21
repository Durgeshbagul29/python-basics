''' 
Take input percentage of a student and print the Grade according to marks:
  a.  81-100 Very Good
  b.  61-80 Good
  c.  41-60 Average
  d.  <=40 Fail
'''
percentage = float(input("Enter your percentage: "))

if percentage <= 100 and percentage >= 81:
  print("Very Good")
elif percentage <= 80 and percentage > 60:
  print("Good")
elif percentage >= 40 and percentage <= 60:
  print("Average")
else:
  print("You are Fail")