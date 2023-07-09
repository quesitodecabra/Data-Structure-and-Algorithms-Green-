heights = []
while True:
  height = int(input())
  if height == 0:
    break
  heights.append(height)

is_ascending = True
for i in range(1, len(heights)):
  if heights[i] < heights[i - 1]:
    is_ascending = False
    break

if is_ascending:
  print("YES")
else:
  print("NO")
