import requests
from config.settings import TROJAN_API_KEY, BULLX_API_KEY

def execute_trade(ca):
    # Example: Execute trade on Trojan
    response = requests.post(
        "https://api.trojan.com/trade",
        headers={"Authorization": f"Bearer {TROJAN_API_KEY}"},
        json={"contract_address": ca, "action": "buy"}
    )
    if response.status_code == 200:
        print("Trade executed successfully")
    else:
        print("Failed to execute trade")