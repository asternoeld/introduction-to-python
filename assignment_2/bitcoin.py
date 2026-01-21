import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    api_key = "d0fd22b40ca93b9874dc84d6f2de57bf6951512698b2226b468ca0ba5e6bc078"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Error fetching data from CoinCap API")

    data = response.json()
    price = float(data["data"]["priceUsd"])
    total = bitcoins * price

    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()
