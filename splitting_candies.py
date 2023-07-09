# input: n(number of candy bags), (num of candies of each bag)
# process: check if the num of candies in each bag n % 2 == 0
# output: YES if divisible, NO if not 
# 3 bags, 4,6,9 candies in each bag
# for i in range n (3)
# 4 % 2 == 0
# 6 % 2 == 0
# 9 % 2 == 1 -> NO

n = int(input())
ans = ""

for i in range(n):
  x = int(input())
  if x < 2 or x % 2 != 0:
    ans = "NO"
    break
  else:
    ans = "YES"
print(ans)
