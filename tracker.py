import requests

def get_eth_balance(address):
    url = f"https://api.blockcypher.com/v1/eth/main/addrs/{address}/balance"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        balance = data["balance"] / 10**18
        print(f"Balance: {balance} ETH")
    else:
        print("Error fetching balance")

if __name__ == "__main__":
    wallet = input("Enter ETH wallet address: ")
    get_eth_balance(wallet)
