'''
Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit  binary numbers  as  its  input  and
then  check  whether  they  are  divisible  by  5  or  not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence
'''

mylist = []
numlist = []
my_input = input('Enter four digits separated by comma : ')
try:
    for i in my_input.split(','):
        numlist.append(i)
    for i in numlist:
        x = int(i, 2)
        if not x % 5:
            mylist.append(i)
    print('The numbers division by 5 are : ')
    print(','.join(mylist))
except:
    print('Invalid input')


