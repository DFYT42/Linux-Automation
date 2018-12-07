#!/usr/bin/python3

print("Hello World!")

impoty sys

a = sys.argv[1]

if a == "1":
  print('a is one')
  print('This is still the then clause of the if statement')

else:
  print('a is',a)
  print('This is still the else clause of the if statement.')
  
print('This is after the if statement.')
