import requests
from config import config

def get_eth_balance(address):
    url = f"{config.BLOCKCYPHER_BASE_URL}/addrs/{address}/balance"
    
    try:
        response = requests.get(url, timeout=config.REQUEST_TIMEOUT)
        
        if response.status_code == 200:
            data = response.json()
            balance = data["balance"] / 10**18
            print(f"Balance: {balance} ETH")
        else:
            print("Error fetching balance")

    except Exception as e:
        if config.DEBUG:
            print(f"Error: {e}")
        else:
            print("Request failed")


if __name__ == "__main__":
    wallet = input("Enter ETH wallet address: ")
    get_eth_balance(wallet)
