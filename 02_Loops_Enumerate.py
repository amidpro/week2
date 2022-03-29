# list_of_numbers = [24, 67, 32, 9, 77]
#
# while list_of_numbers:
#     popped = list_of_numbers.pop()
#     if popped % 2 == 0:
#         print(popped, 'is even')
#         continue
#     else:
#         print(popped, 'is odd')
#     print(popped, 'doubled is', popped * 2)

names = ['Rod', 'Jane', 'Freddie']
# lists variable

# while list_of_names:
#     popped_names = list_of_names.pop()
#     if popped_names == 'Jane':
#         break
#     print(popped_names)


for name in names:
    print(name.upper())
# converts names into UPPERCASE

for index, name in enumerate(names):
    print(index, name.upper())
# prints numbered list starting from 0 (default index)
# The enumerate() function allows you to loop over an iterable object and keep track of how many iterations have occurred.

for index, name in enumerate(names):
    print(index, name.upper())
    if name.upper() == 'ROD':
        names[index] = 'Zippy'
        print(names[0])
# replacing names in List, using 'Zippy" to replace 'ROD' - [0] position(index)

print(names)
# prints new list of names (replacing 'ROD' with 'Zippy'