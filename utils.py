# utils.py

import re

def is_valid_eth_address(address: str) -> bool:
    """
    Basic ETH address validation (0x + 40 hex chars)
    """
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return bool(re.match(pattern, address))


def wei_to_eth(wei: int) -> float:
    """
    Convert Wei to ETH
    """
    return wei / 10**18


def format_balance(balance: float) -> str:
    """
    Pretty formatting
    """
    return f"{balance:.6f} ETH"
