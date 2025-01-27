# Currency Converter

A Python-based currency converter that allows users to convert USD to a selected currency using real-time exchange rates from the FreeCurrencyAPI.

## Features

- Retrieves live exchange rates from the FreeCurrencyAPI
- Allows users to convert USD to a specified currency
- Displays a list of valid currencies for selection
- Implements error handling for invalid inputs and API request failures
- Provides multiple attempts for users to enter a valid currency

## Technologies Used

- **Python**
- **Requests** (for API calls)
- **JSON** (for parsing API responses)

## How It Works

1. The program retrieves live exchange rates from the FreeCurrencyAPI.
2. The user selects a currency from the list of available options.
3. The user enters an amount in USD to convert.
4. The program calculates and displays the converted amount based on the current exchange rate.

## Installation & Setup

### Clone the repository
```bash
git clone https://github.com/ChunkyMonkey11/Currency-Converter.git
cd Currency-Converter
