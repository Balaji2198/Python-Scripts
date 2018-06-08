import requests

def calculate(from_value, to_value , currency_value, amount):
	total_value = currency_value * float(amount)
	print (amount +" "+ from_value +" = "+ str(total_value) + " " + to_value)

def convert(from_value, to_value, amount):
	url = "http://free.currencyconverterapi.com/api/v3/convert?q="
	fetch = from_value +"_"+ to_value
	final_url = url + fetch + "&compact=ultra"
	data = requests.get(final_url)
	read = data.json();
	currency_value = read[fetch]
	calculate(from_value, to_value, currency_value, amount)

def get_input():
	from_value = input("Enter the currency to convert from: ").upper()
	to_value = input("Enter the currency to convert to: ").upper()
	amount = input("Enter the amount to convert: ")
	convert(from_value, to_value, amount)

if __name__ == "__main__":
	get_input()
