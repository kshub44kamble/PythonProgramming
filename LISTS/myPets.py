#!/usr/bin/env python3

#For example, the following program lets the user type in a pet name 
#and then checks to see whether the name is in a list of pets.

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
	print('I do not have a pet named ' + name)
else:
	print(name + ' is my pet.')

