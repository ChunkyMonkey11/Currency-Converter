'''
This is code to copy and paste into the other file that 
is a test that should always work as long as this code runs then the program works
'''

# Setting variable to retrive currencies 
Currencies = get_currency()

# Statment that works
if Currencies:
    # Print the entire JSON response in a cleaner format
    print(json.dumps(Currencies, indent=4))

    # Extract usd exchange rate
    usd_rate = Currencies["data"]["USD"]

    # Print the exchange rate of USD
    print("Exchange rate for USD:", usd_rate)