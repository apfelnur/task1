def sort_list(l1, l2):
 
    zp = zip(l2, l1)
 
    z = [x for _, x in sorted(zp)]
 
    return z
 
x = [1, 4, 6]
y = [11, 33, 22]
 
print(sort_list(x, y))
