s = ['t', 'a', 'p', 'r', 'e', 'u', 'm', 'e', 'o', 'i']  # created a list, s, to use for testing outside of sandbox

# 'x' = 0                                               # x instead of 'x'; single or double quotations specifies things as a string instead of a variable
# 'v' = ['a' , 'e' , 'i' , 'o' , 'u']                   # v instead of 'v'; again, the quotations make v a string insead of a variable pointing to a list
# for char in s:                              
#      if char in 'v':                                  # same, v instead of 'v'
#      x += 1                                           # this is improperly indented; after an if statement, you have to indent anything that is included in the if clause
# print(x)                                              # this is why you were getting 10.  It was doing x += 1 for every char


x = 0
v = ['a' , 'e' , 'i' , 'o' , 'u']
for char in s:
    if char in v:
        x += 1
print(x)