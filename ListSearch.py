'''
Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list
'''

def listSearch(mylist, mysearch):
    for i in range(len(mylist)):
        if mylist[i] == mysearch:
            return True
    return False


mylist = ['r', 'a', 'm', 'y', 'a']
mysearch = 'm'
if listSearch(mylist, mysearch):
    print("The item ", mysearch, "is found in the list")
else:
    print("The item ", mysearch, "is not found in the list")