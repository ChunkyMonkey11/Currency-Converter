import warnings
warnings.filterwarnings("ignore")
import requests
import json

def get_currency():
    # Define the API endpoint URL
    url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_m4Wwm86wa4UC3DOVeN7nYRMv0zVb1LQetDHRrbMW'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            CURRENCIES = response.json()
            return CURRENCIES
    # Handle any network-related errors or exceptions
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None
    
# Setting variable to retrive currencies 
Currencies = get_currency()


if Currencies:

    # Print the entire JSON response in a cleaner format
    print(json.dumps(Currencies, indent=4))

    # Extract usd exchange rate
    usd_rate = Currencies["data"]["USD"]

    # Print the exchange rate of USD
    print("Exchange rate for USD:", usd_rate)

    

        






