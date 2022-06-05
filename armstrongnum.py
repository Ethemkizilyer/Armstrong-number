#Armstrong Numbers
a=input()
if a.isdigit():
  c=int(a)
  n=len(a)
  topl=0
  for i in a:
    topl += int(i)**n
  if topl==int(c):
    print("{} is an Armstrong number".format(int(a)))
  else:
    print("{} is not an Armstrong number".format(int(a)))
else:
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")