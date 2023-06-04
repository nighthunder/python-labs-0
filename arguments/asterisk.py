'''
Arbitrary positional arguments
'''

'''
For arbitrary positional argument, an asterisk (*) is placed before
a parameter in function definition which can hold non-keyword variable-length arguments. 
These arguments will be wrapped up in a tuple. 
Before the variable number of arguments,
 zero or more normal arguments may occur.
'''

def add(*b):
    result=0
    for i in b:
         result=result+i
    return result

print (add(1,2,3,4,5))
#Output:15
print (add(10,20))
#Output:30
'''
Output:
('numbers', 5)
('colors', 'blue')
('fruits', 'apple')
'''