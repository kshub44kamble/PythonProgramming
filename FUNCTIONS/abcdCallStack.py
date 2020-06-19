def a():
	print('a() starts')
	b()
	d()
	print('a() returns')

def b():
	print('b() starts')
	c()
	print('b() returns')

def c():
	print('c() starts')
	print('c() returns')

def d():
	print('d() starts')
	print('d() returns')

a()

#The call stack isn't stored in a variable in your program; rather Python handles it behind the scenes.
#When your program calls a function, Python creates a frame object on th top of the stack.

