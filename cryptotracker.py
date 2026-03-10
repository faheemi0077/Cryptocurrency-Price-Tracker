import requests
def get_price(name, currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": name.lower(), "vs_currencies": currency}
    response = requests.get(url, params=params)
    data = response.json()
    return data.get(name.lower(), {}).get(currency)
decision1 = input("Would you like to see the current price of a specific cryptocurrency? ")
lowered = decision1.lower()
if lowered != "yes":
    print("Okay, ending the program. ")
else:
    while lowered == "yes":
        coinname = input("Which cryptocurrency would you like to see the price of (by name)?")
        #logic of fetching the coins price
        price = get_price(coinname)
        if price == None:
            print("Sorry, we could not find the price of that coin! ")
        else:
            print(f"The price of {coinname} coin is ${price:,.2f}! ")
        decision1 = input("Would you like to see the price of a specific cryptocurrency?")
        lowered = decision1.lower()
        