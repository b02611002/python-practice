def checkDouble(s):
	l = len(s)
	for x in range(l-1):
		if (s[x].lower() == s[x+1].lower()): 
			print("TRUE")
			return
	print("FALSE")

checkDouble(input("Enter a string (with quotation marks):"))
