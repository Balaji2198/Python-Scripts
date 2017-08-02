#!/usr/share/env python3
#Python Program - Print Prime Numbers in a given range
		
while True:
	choice = input("Do you want to continue? Press y or n: ")
	if choice == 'n':
		break
	else:				
		lower_number = int(input("Enter a starting number: "))
		upper_number = int(input("Enter a ending number: "))
		print("\nPrime Numbers between the given range:")
		for num in range(lower_number, upper_number+1):
			if num > 1:
				for i in range(2, num):
					if(num%i)==0:
						break
				else:
					print(num)
