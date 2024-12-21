# Collections => Basically this allow us to stored multiple items in a sinlge variable. 

'''
*** List :- 
list can be stored in index form start always from zero. 
list can be maintain items order by user 
lists are mutable It means we can changed index value of items.
Allowed duplicate values, stored any type of data and we can also stored different types of data in single list.

Syntax =>   variable_name = ["Value1","Value2","Value3"]
'''
# Create list as student names in class
stud_name = ["Durgesh","Gaurav","Vrushali","Raj"]
print(stud_name)

# len() :- lenght of the list or returns the number of items which is present in list.
print("Total student present in this list:", len(stud_name))

# reverse() :- Reverse of current list
stud_name.reverse()
print("List after reverse:", stud_name)

# check student present or not (in / not in)
if "Ram" in stud_name:
  print("Ram is present")
else:
  print("Ram is not present")


''' Accessing items of a list '''
# 1) indexing => By using index value is positive either negative.
print("Index 2:", stud_name[2])
print("Index -1:", stud_name[-1]) # It will be work in reverse order.

# 2) range of indexs => passed start and end index values :- start (inclusive) : end (exclusive)
print(stud_name[2:4])
# we also used negative index 
print(stud_name[-3:-1])


'''Adding items in list '''
# 1) append() => it will be add end of list
stud_name.append("Deepu")
print("After append:", stud_name)

# 2) insert() => to add item on particular index :- (index_number, item)
stud_name.insert(2, "Jyotsana")
print("After insert:", stud_name)

# 3) extend() => add second list end of the current list It means concatination of two lists.
teacher_name = ["Rajiv","Mayur"]
stud_name.extend(teacher_name)
print("After extend:", stud_name)


''' Removing items from a list '''
# 1) remove() => it will be remove specified item from list
stud_name.remove("Raj")
print("After removing:", stud_name)

# 2) pop() => delete last item from list or if passed index number then its remove at given index item.
print("After used pop without index number:", stud_name.pop(),end="")
print(stud_name)
print("After used pop witt index number 2:", stud_name.pop(2),end="")
print(stud_name)


''' Changing item in a list '''
# 1) at an index() => updating item by using index number
stud_name[1] = "Digmber"
print(stud_name)

# 2) in a range() => updating items by using range values
stud_name[1:3] = ["Pawan","Ganesh"]
print(stud_name)


''' Sorting a list '''
# 1) Ascending => sorting in A - Z and 0 - 9 form  :- sort()
stud_name.sort()
print("After ascending sorting:", stud_name)

# 2) Descending => sorting in Z - A and 9 - 0 form  :- sort(reverse = True)
stud_name.sort(reverse=True)
print("After descending sorting:", stud_name)


''' List Comprehension'''
# When we want to make a new list from items of an existing list based on such condition.  
# List Travelsing => Traditional way :- 
list = [22,45,11,20,2,35,6,66]
new_list = []
for i in list:
  if i > 25:
    new_list.append(i)
print("New list traditional method:", new_list)

# Model way (List Comprehension) => 
# list= [variable_declartion for variable in list condition]
new_list= [i for i in list if i >= 20]
print("New list for number:", new_list)

# For Str :- 
new_list = [student for student in stud_name if "s" in student]
print("New list for str:", new_list)

# Copy all list => copy() function
new_list = stud_name.copy()
print("New list using copy fun:", new_list)

# Copy all list => concat + operator
new_list = stud_name + new_list
print("New list using concat:", new_list)