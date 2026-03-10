# Cryptocurrency Price Checker

This project is a simple command-line tool that retrieves the current price of a cryptocurrency using the CoinGecko API. The user can input the name of a cryptocurrency and the program will return its latest price in USD.

## How It Works

1. The program prompts the user to decide if they want to check a cryptocurrency price.
2. If the user chooses yes, they are asked to enter the name of a cryptocurrency.
3. The program sends a request to the CoinGecko API to retrieve the latest price data.
4. The current price is displayed in USD.
5. The user can continue checking additional cryptocurrencies until they choose to exit.

## Features

- Command-line interface for quick price lookups
- Real-time cryptocurrency prices
- Uses the CoinGecko public API
- Handles invalid or unsupported coin names

## Requirements

- Python 3
- 'requests' library
