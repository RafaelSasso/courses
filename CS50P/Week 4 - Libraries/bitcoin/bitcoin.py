import requests
import sys

def main():
    if(len(sys.argv)==1):
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=e0bf7758d71ef1371b4e035bb3f3c85e17ddf568df9dfb5b1874902cbd1d1ab8")
    except requests.RequestException:
        sys.exit("Couldn't connect to API")

    o = response.json()
    price = float(o["data"]["priceUsd"])

    print(f'${(price*n):,.4f}')


if __name__ == "__main__":
    main()
