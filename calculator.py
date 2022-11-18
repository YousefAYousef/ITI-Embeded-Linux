print("*************************************************************")
print(" ")
print(" ")
print("\t Welcom to ITI calculator :)")
print(" ")
print(" ")
print("*************************************************************")
print(" ")

mod = input("\t Hit 1 for Scintific mode OR 2 for Programmer mode, 0 to EXIT")
mod = int(mod)

if mod == 1:
	print(" ")
	print("\t Welcome to Scintific MODE :)")
	print("\t Here you can do some operations: ADD(+), Sub(-), Multply(*), Divide(/) , power (^)")
	print(" ")
	print("\t Your input format first number , operation, second number")
	print("\t PLEASE, Press ENTER after each input")
	print(" ")
	print(" ")
	
	num1 = input("Enter your First number: ")
	op = input("Enter your the operation you want to apply: ")
	num2 = input("Enter your Second number: ")
	num1 = int(num1)
	num2 = int(num2)
	
	if op == "+" :
		print("{} + {} = {}".format(num1, num2 , num1 + num2))
	elif op == "-" :
		print("{} - {} = {}".format(num1, num2 , num1 - num2))
	elif op == "*" :
		print("{} * {} = {}".format(num1, num2 , num1 * num2))
	elif op == "^" :
		print("{} * {} = {}".format(num1, num2 , pow(num1 , num2)))
	elif op == "/" :
		if num2 == 0:
			print("ERORR, cant divide by zero")
		else:
			print("{} / {} = {}".format(num1, num2 , num1 / num2))

elif mod == 2:
	print(" ")
	print("\t Welcome to PROGRAMMER MODE :)")
	print("\t Here you can do conver decimal to: BIN , HEX , and OCT")
	print(" ")
	print("\t Your input format first number , operation, second number")
	print(" ")
	print(" ") 
	op = input("Choose the number of yoir operation : \n 1- DECIMAL TO BIN \n 2- DECIMAL TO HEX \n 3- DECIMAL TO 0CT  \n 4- BINARY TO DECIMAL \n 5- HEXA TO DECIMAL \n 6-OCTA TO DECIMAL \n")
	op = int(op)
	num = input("Enter your number: ")
	num = int(num)
	if op == 1 :
		print(bin(num))
	elif op == 2 :
		print(hex(num))
	elif op == 3 :
		print(oct(num))
	elif op == 4 :
		print(int(num))
	elif op == 5 :
		print(int(num, 16))
	elif op == 6 :
		print(int(num, 8))
elif mod == 0:
	print("EXIT Calculator, Good Bye :(")