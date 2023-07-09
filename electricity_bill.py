last_month, this_month = map(int, input().split())
total_voltage = this_month - last_month

ans = 0
if (total_voltage <= 50):
  ans = total_voltage * 1484
elif(total_voltage <= 100):
  ans = 50*1484 + (total_voltage-50)*1533
elif(total_voltage <= 200):
  ans = 50*1484 + 50*1533 + (total_voltage -100)*1786
elif(total_voltage <= 300):
  ans = 50*1484 + 50*1533 + 100*1786 + (total_voltage - 200)*2242
elif(total_voltage <= 400):
  ans = 50*1484 + 50*1533 + 100*1786 + 100*2242 + (total_voltage - 300)*2503
else:
  ans = 50*1484 + 50*1533 + 100*1786 + 100*2242 + 100*2503 + (total_voltage - 400)*2587
  
print(int(ans * 1.1))
