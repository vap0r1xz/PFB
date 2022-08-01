#Call api to get the exchange rate
import requests
def get_exchange_rate():
    # In case alphavantage is down, function will return false
    try:
        # Use API to get the data
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=ZLPW520HQGKTSS7M'
        r = requests.get(url)
        data = r.json()

        # Narrow data down to element that is needed
        exchange_rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        
        return exchange_rate
    except:
        return False