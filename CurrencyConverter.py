import warnings
warnings.filterwarnings("ignore")
import requests


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
    

# Function to retrieve all valid currencies for later usage.
def get_valid_currencies(json_data):
    
    # Extract the keys from the 'data' dictionary
    return list(json_data["data"].keys())

# Manually creating a dictonary with valid currencies in a non abbreivated format
FULL_CURRENCIES_NAMES = {
    "AUSTRALIAN DOLLAR": "AUD",
    "BULGARIAN LEV": "BGN",
    "BRAZILIAN REAL": "BRL",
    "CANADIAN DOLLAR": "CAD",
    "SWISS FRANC": "CHF",
    "CHINESE YUAN": "CNY",
    "CZECH KORUNA": "CZK",
    "DANISH KRONE": "DKK",
    "EURO": "EUR",
    "BRITISH POUND": "GBP",
    "HONG KONG DOLLAR": "HKD",
    "CROATIAN KUNA": "HRK",
    "HUNGARIAN FORINT": "HUF",
    "INDONESIAN RUPIAH": "IDR",
    "ISRAELI SHEKEL": "ILS",
    "INDIAN RUPEE": "INR",
    "ICELANDIC KRONA": "ISK",
    "JAPANESE YEN": "JPY",
    "SOUTH KOREAN WON": "KRW",
    "MEXICAN PESO": "MXN",
    "MALAYSIAN RINGGIT": "MYR",
    "NORWEGIAN KRONE": "NOK",
    "NEW ZEALAND DOLLAR": "NZD",
    "PHILIPPINE PESO": "PHP",
    "POLISH ZLOTY": "PLN",
    "ROMANIAN LEU": "RON",
    "RUSSIAN RUBLE": "RUB",
    "SWEDISH KRONA": "SEK",
    "SINGAPORE DOLLAR": "SGD",
    "THAI BAHT": "THB",
    "TURKISH LIRA": "TRY",
    "US DOLLAR": "USD",
    "SOUTH AFRICAN RAND": "ZAR"
}
FULL_VALID_CURRENCIES = list(FULL_CURRENCIES_NAMES.keys())

# Getting users desired currency with attempt handling
def get_desired_currency():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        
        desired_currency = input("What is the currency that you would like to convert USD into? ").upper()

        if desired_currency in VALIDCURRENCIES:
            return desired_currency

        elif desired_currency in FULL_VALID_CURRENCIES:
            # Return the corresponding abbreviation
            return FULL_CURRENCIES_NAMES[desired_currency]
        else:
            attempts += 1
            print(f"Invalid currency. You have {max_attempts - attempts} attempts left.")
            print(f"Valid currencies: {', '.join(VALIDCURRENCIES)}")

    # print("Too many invalid attempts. Returning to the main menu...")
    return None



# Retriving currencies from api
retrieved_currencies = get_currency() 

# Calling function to retrieve valid currencies for user to access from.
VALIDCURRENCIES = get_valid_currencies(retrieved_currencies)

# Main code
if retrieved_currencies:
    print("\n===============================")
    print("🌍 Welcome to the Currency Converter 🌍")
    print("===============================\n")

    # Prompting user for desired currency
    users_currency = get_desired_currency()

    # Checking to see if their is no currency to convert and handling the key error.
    if users_currency is None:
        print("❌ Too many invalid attempts. Returning to the main menu...")
        exit()

    # Retriving rate of desired currency
    desired_rate =  retrieved_currencies["data"][users_currency]
    print("\n")

    # Prompting user for how much USD they want to convert.
    while True:
        try:
            amount_pre_conversion = float(input(f"💵 Enter the amount in USD to convert into {users_currency}: $"))
            if amount_pre_conversion <= 0:
                print("❌ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

    # Calculating how much the USD is worth after conversion
    amount_post_conversion = amount_pre_conversion * desired_rate



    # print(f"The desired currency is {users_currency}, and the conversion rate from usd to that currency is {desired_rate}")  
    print("\n===============================")
    print(f"💰 Conversion Summary 💰")
    print(f"👉 {amount_pre_conversion:.2f} USD is equivalent to {amount_post_conversion:.2f} {users_currency}")




