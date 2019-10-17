'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡-Y-1.
Example:Suppose the following inputs are given to the program:3,5
Then, the output of the program should be:[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''


x = int(input("Input number of rows: "))
y = int(input("Input number of columns: "))
multi_list = [[0 for col in range(y)] for row in range(x)]

for r in range(x):
    for c in range(y):
        multi_list[r][c] = r * c

print(multi_list)