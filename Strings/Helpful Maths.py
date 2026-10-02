s=input()
number=[i for i in s if i !='+']
number.sort()
print('+'.join(number))
