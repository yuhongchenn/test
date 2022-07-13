# form objprint import op
list1 = [1,2,3,4,5,'s']
list2 = [1,3,4,5,6,6,]

# op(print (dict(zip(list1, list2))))

print (dict(zip(list1, list2)))
# {1: 1, 2: 3, 3: 4, 4: 5, 5: 6, 's': 6}

print (list1.append(list2))
list1.extend(list2)
list1.extend((1,22222,3))
list1.append((1,23))
print (list1)