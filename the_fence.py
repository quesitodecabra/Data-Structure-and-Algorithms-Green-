# Write a program to draw Harry's square fence with length n. Signed fence denoted by the character '*', the plots inside the fence are spaces.
# input n
# print the first row '*' * n
# print the middle rows( without the first and last row):
# for i in range(n-2):
#  print('*' + ' ' * (n-2) + '*')
	
n = int(input())

print('*' * n)  # First row

for i in range(n - 2):  # Middle rows
    print('*' + ' ' * (n - 2) + '*')
	
print('*' * n)  # Last row
