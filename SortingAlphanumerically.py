'''
Write a program that accepts a sequence of whitespace separated words as input and   prints   the   words   after
 removing   all   duplicate   words   and   sorting   them alphanumerically.
 Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

mystr = input('Enter sequence of words : ')
myset = set()
mylist = []
for i in mystr.split(' '):
    myset.add(i)
print(myset)
sortedSet = sorted(myset)
print(sortedSet)
for i in sortedSet:
    mylist.append(i)
print(' '.join(mylist))