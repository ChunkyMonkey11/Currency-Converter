import warnings
warnings.filterwarnings("ignore")
import requests
import json

# Function to get the currencies
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
    




# Retriving currencies from api
retrieved_currencies = get_currency()



# Function to retrieve all valid currencies for later usage.
def get_valid_currencies(json_data):
    
    # Extract the keys from the 'data' dictionary
    return list(json_data["data"].keys())


# Calling function to retrieve valid currencies for user to access from.
VALIDCURRENCIES = get_valid_currencies(retrieved_currencies)


# User Inputted Curerency.
def get_desired_currency():
    # Prompt user for desired currency
    Desired_Currency = input("What is the currency that you would like to convert USD into? ").upper()

    # Checking if the currency the user wants is valid.
    if Desired_Currency in VALIDCURRENCIES:
        return Desired_Currency
    else:
        # Error message
        print(f"Invalid currency. Please choose from the following: {', '.join(VALIDCURRENCIES)}")


    
if retrieved_currencies:
    users_currency = get_desired_currency()
    print(f"The desired currency is {users_currency}")  

