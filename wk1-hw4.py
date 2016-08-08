length=input("Length ?")

def Fibonacci_for_version(n):
	list=[1,1]
	if n==1:	print(1)
	elif n==2:	print(1,1)
	else:
		for i in range(0,n-2):
			list.append(list[-1]+list[-2])
		print(list)
			
print("\n Fibonacci_for_version(%d): ") % length
Fibonacci_for_version(length)



def Fibonacci_while_version(n):
	list=[1,1]
	if n==1:	print(1)
	elif n==2:	print(1,1)
	else:
		while (len(list) < n):
			list.append(list[-1]+list[-2])
		print(list)

print("\n Fibonacci_while_version(%d): ") % length
Fibonacci_while_version(length)
