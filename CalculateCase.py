'''
Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of  upper  case letters and lower case letters
'''


mystr = input("Enter a string : ")
mydict = {'uppercase': 0, 'lowercase': 0}
for i in mystr:
    if i.isupper():
        mydict['uppercase'] += 1
    elif i.islower():
        mydict['lowercase'] += 1
    else:
        pass
print('Number of upper case characters : ', mydict['uppercase'])
print('Number of lower case characters : ', mydict['lowercase'])