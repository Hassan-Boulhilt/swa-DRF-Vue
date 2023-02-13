import requests

def main():
    

    url = "https://api.apilayer.com/exchangerates_data/convert?to=MAD&from=USD&amount=1"

    payload = {}
    headers= {
        "apikey": "Your api key"
    }
    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.json()
    print("Status Code:", status_code)
    
    

    print(f"{result['query']['amount']} {result['query']['from']} to {result['query']['to']} is: {result['info']['rate']}" )


if __name__=='__main__':
    main()