# To remove spaces from both sides of a string...

city = input("Enter your city Name:")
scity= city.strip()
if scity == "Enugu":
	print("Hello Enugu.... 042")
elif scity == "Akwa":
	print("Hello Akwa..... Umu Otu")
elif scity == "PH":
	print("Hello PH...... Oil Money")
else:
	print("your entered city is invalid")

