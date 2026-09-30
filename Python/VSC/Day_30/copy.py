# Shallow - it will copy outer,inner but inner will be share and accessing with new copied
# Deepcopy- it will copy outer and inner without sharing and accessing each other
import copy
l1 = [1, 2, [10, 20]]
l2 = copy.coopy(l1)
l2 = copy.deepcopy(l1)
print(l1, l2)
l2[0] = 100
l2[2][0] = 1000
print(l1, l2)
