a = [] # empty list
a = [1, 10, 6, 8] # list of integer
a = [1,
,6.3] # list with mixed datatype

print(a[2]) # print element index 2
print(a[:2]) # print first element to index 2
print(a[2:4]) # print from index 2 to 4 (slice of list)

a[2] = 10 # change the 2nd item
a[2:4] = [1, 10, 6] # change 2nd to 4th items

a.append(10) # add one item to last element
a.extend([1, 10, 6]) # add several items to last element

c = a + b # join list a and b into c
a.extend(b) # add several items b into a