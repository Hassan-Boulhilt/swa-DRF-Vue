import requests

def main():
    

    url = "https://api.apilayer.com/exchangerates_data/latest"

    payload = {}
    headers= {
        "apikey": "Your api key"
    }
    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.json()
    print("Status Code:", status_code)
    
    

    print(result)


if __name__=='__main__':
    main()