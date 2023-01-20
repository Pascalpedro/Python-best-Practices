# Program to find the biggest of 3 given numbers....       

n1 = int(input("Enter First Number:"))                    
n2 = int(input("Enter Second Number:"))
n3 = int(input("Enter Third Number:"))                  
if n1>n2 and n2>n3:                     
	print("Biggest Number is:", n1)
elif n2>n3:
	print("Biggest Number is:", n2)
else:                                                     
	print("Biggest Number is:", n3)                    
