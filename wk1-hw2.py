def pattern(n):

	rowNum = 1
	space = n-1

	while(rowNum<n):
		line = ' '*space
		temp = 1
		while(temp <= rowNum):
			line += str(temp)
			temp+=1
		
		temp = rowNum-1	
		while(temp >= 1):
			line += str(temp)
			temp-=1	

		print(line)		
		
		rowNum+=1
		space-=1
		

	while(rowNum>0):
                line = ' '*space
                temp = 1
                while(temp <= rowNum):
                        line += str(temp)
                        temp+=1

                temp = rowNum-1
                while(temp >= 1):
                        line += str(temp)
                        temp-=1

                print(line)

                rowNum-=1
                space+=1


pattern(input("Size ? "))
