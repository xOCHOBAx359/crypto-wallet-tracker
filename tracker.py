import requests
from config import config
from utils import is_valid_eth_address, wei_to_eth, format_balance


def get_eth_balance(address):
    if not is_valid_eth_address(address):
        print("Invalid ETH address")
        return

    url = f"{config.BLOCKCYPHER_BASE_URL}/addrs/{address}/balance"

    try:
        response = requests.get(url, timeout=config.REQUEST_TIMEOUT)

        if response.status_code == 200:
            data = response.json()
            balance = wei_to_eth(data["balance"])
            print(f"Balance: {format_balance(balance)}")
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
