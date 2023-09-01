# GraphQL query to fetch details of a specific token by its contract address (id)
FETCH_V3_TOKEN_QUERY = """
query FetchToken($id: ID!) {
    token(id: $id) {
        id
        symbol
        name
        decimals
    }
}
"""

FETCH_V3_TOKEN_LIST = """
query FetchTokenList {
  tokens(where: {_totalValueLockedUSD_gte: "1000000"}) {
    id
    symbol
    name
    decimals
  }
}
"""
# GraphQL query to fetch all pools that involve a specific token by its contract address (id)
FETCH_V3_PAIRS_FOR_TOKEN_QUERY = """
query FetchPairsForToken($id: ID!) {
    pools(where: {token0: $id}) {
        id
        token0 {
            id
            symbol
            name
        }
        token1 {
            id
            symbol
            name
        }
        tick
        sqrtPrice
    }
}
"""

# gql_queries.py

FETCH_V3_SWAP_TRANSACTIONS_QUERY = """
query swaps($pairId: ID!, $first: Int = 10, $orderBy: String = "timestamp", $orderDirection: String = "desc") {
  swaps(where: { pool: $pairId }, first: $first, orderBy: $orderBy, orderDirection: $orderDirection) {
    id
    timestamp
    amount0
    amount1
    pool {
      token0 {
        id
        symbol
      }
      token1 {
        id
        symbol
      }
    }
    transaction {
      id
    }
  }
}
"""

# Add this query at the end of the file
FETCH_V3_SWAP_TRANSACTIONS_FOR_TIMESTAMP_QUERY = """
query FetchSwapsForPairAtTimestamp($pair_id: ID!, $start_time: BigInt!, $end_time: BigInt!) {
    swaps(
        where: { pool: $pair_id, timestamp_gte: $start_time, timestamp_lte: $end_time },
        orderBy: timestamp
    ) {
        id
        timestamp
        amount0
        amount1
        pool {
            token0Price
            token1Price
        }
        amountUSD
    }
}
"""

FETCH_V3_SWAPS_TOKEN_IN_TOKEN_OUT = """
query FetchSwapsTokenInTokenOut($token_id: ID!, $start_time: BigInt!, $end_time: BigInt!) {
  swaps1: swaps(
    where: {tokenIn: $token_id, timestamp_gte: $start_time, timestamp_lte: $end_time},
    orderBy: timestamp
    orderDirection: desc
  ) {
      id
        timestamp
    	amountIn
        amountInUSD    
  }
  swaps2: swaps(
    where: {tokenOut: $token_id, timestamp_gte: 1692997679, timestamp_lte: 1693540171},
    orderBy: timestamp
  ) {
      id
        timestamp
    	amountOut
        amountOutUSD    
  }
}
"""

FETCH_V3_SPECIFIC_PAIR = """
query FetchSpecificPair($token0_id: ID!, $token1_id: ID!) {
  pool0: pools(where: {token0: $token0_id, token1: $token1_id}) {
    id
    token0 {
      id
      symbol
      name
    }
    token1 {
      id
      symbol
      name
    }
    token0Price
    token1Price
    volumeUSD
  }
  pool1: pools(where: {token0: $token1_id, token1: $token0_id}) {
    id
    token0 {
      id
      symbol
      name
    }
    token1 {
      id
      symbol
      name
    }
    token0Price
    token1Price
    volumeUSD
  }
}
"""
