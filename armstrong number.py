
#ARMSTRONG NUMBER
num = int(input("enter a num:"))
sum = 0
temp = num
while temp > 0:
  digit = temp % 10
  sum += digit ** 3
  temp //= 10
if num == sum:
  print(num,"is armstrong")
else:
  print(num,"not armstrong")









