'''
Write a program that calculates and prints the value according to the
given formula:Q = Square root of [(2 * C * D)/H]Following are the fixed values of C and H: C is 50.
H is 30.D  is  the  variable  whose  values  should  be  input  to  your  program  in  a  comma-separated sequence

Example:
    Let  us  assume  the  following  comma  separated
    input  sequence  is  given  to  the program:100,150,180
    The output of the program should be:18,22,24
'''

import math
c = 50
h = 30
result = []
user_input = input('Enter the numbers separated by comma : ')
try:
    items = [x for x in user_input.split(',')]
    for d in items:
        ans = round(math.sqrt(2 * c * float(d)/h))
        result.append(str(ans))
    print(','.join(result))
except:
    print('Invalid input')