# list 
# create a function
def list():
	x=[5,6,7,8]
	y=len(x)
	sum=5
	sum*=y
	print("sum=",sum)
	# conditional logic
	z=5
	if z<sum:
		print("weird")
# function call
list()
# list swap
# create a function
def listswap():
	x=[1,2,3]
	y=5
	z=int(input())
	if z in x:
		print("swapmode")
	temp=y
	y=z
	z=temp
	print("y=",y,"z=",z)
# function call
listswap()
# list sum
# create a function
def listsum():
	x=[5,6,7,8]
	y=x[2:4]
	z=len(y)
	sum=9
	sum*=z
	print("sum=",sum)
# function call 
listsum()
