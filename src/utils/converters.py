# utils/converters.py

def wei_to_eth(wei_value):
    """
    Convert WEI to ETH
    """
    return wei_value / 1e18


def eth_to_wei(eth_value):
    """
    Convert ETH to WEI
    """
    return eth_value * 1e18


def token_to_decimal(value, decimals):
    """
    Convert token value to its decimal representation
    """
    return value / (10 ** decimals)


def decimal_to_token(value, decimals):
    """
    Convert decimal value to its token representation
    """
    return value * (10 ** decimals)


def format_price(price):
    """
    Format price to a reasonable number of decimal places
    """
    return "{:.8f}".format(price)


def format_volume(volume):
    """
    Format volume to a reasonable number of decimal places
    """
    return "{:.4f}".format(volume)
