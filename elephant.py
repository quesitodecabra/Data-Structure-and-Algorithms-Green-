elephant_start = 0
distance = int(input())

# if the distance is divisible by 5, that's the total amount of steps to take
if(distance % 5 == 0):
    steps = distance // 5
else:
# else if the nguyên part is disvisible by by 5
# the leftover would be be 1,2,3,4
# but they all mean you need need1 more step to finnish
# apart from the 5s steps already calculated
    steps = distance // 5 + 1
print(steps)