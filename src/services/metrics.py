# services/metrics.py

def calculate_liquidity(token0_reserves, token1_reserves):
    return token0_reserves * token1_reserves

def calculate_trading_volume(amount0In, amount1In):
    return amount0In + amount1In

def calculate_price(token0_reserves, token1_reserves):
    try:
        token0_reserves = float(token0_reserves)
        token1_reserves = float(token1_reserves)
    except ValueError:
        return 0
    
    if token0_reserves == 0:
        return 0
    return token1_reserves / token0_reserves

def calculate_price_from_swaps(swaps):
    total_amount_in = 0
    total_amount_out = 0

    for swap in swaps:
        total_amount_in += float(swap['amount0In'])
        total_amount_out += float(swap['amount1Out'])
    
    if total_amount_in == 0:
        return 0

    return total_amount_out / total_amount_in
