'''
Arbitrary positional arguments
'''

'''
For arbitrary positional argument, a double asterisk (**) 
is placed before a parameter in a function which can hold keyword variable-length arguments.
'''

def fn(**a):
    for i in a.items():
        print (i)
fn(numbers=5,colors="blue",fruits="apple")
'''
Output:
('numbers', 5)
('colors', 'blue')
('fruits', 'apple')
'''