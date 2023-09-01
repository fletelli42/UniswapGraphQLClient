# GraphQL query to fetch details of a specific token by its contract address (id)
FETCH_TOKEN_QUERY = """
query FetchToken($id: ID!) {
    token(id: $id) {
        id
        symbol
        name
    }
}
"""

FETCH_TOKEN_LIST = """
query FetchTokenList {
  tokens(where: {tradeVolumeUSD_gt: "1000000000"}) {
    id
    symbol
    name
    decimals
    tradeVolumeUSD
  }
}
"""

# GraphQL query to fetch all pairs that involve a specific token by its contract address (id)
FETCH_PAIRS_FOR_TOKEN_QUERY = """
query FetchPairsForToken($id: ID!) {
    pairs(where: {token0: $id}) {
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
        reserve0
        reserve1
    }
}
"""

# gql_queries.py

FETCH_SWAP_TRANSACTIONS_QUERY = """
query swaps($pairId: ID!, $first: Int = 10, $orderBy: String = "timestamp", $orderDirection: String = "desc") {
  swaps(where: { pair: $pairId }, first: $first, orderBy: $orderBy, orderDirection: $orderDirection) {
    id
    timestamp
    amount0In
    amount0Out
    amount1In
    amount1Out
    pair {
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

FETCH_SWAP_TRANSACTIONS_FOR_TIMESTAMP_QUERY = """
query FetchSwapsForPairAtTimestamp($pair_id: ID!, $start_time: BigInt!, $end_time: BigInt!) {
    swaps(
        where: { pair: $pair_id, timestamp_gte: $start_time, timestamp_lte: $end_time },
        orderBy: timestamp
    ) {
        id
        timestamp
        amount0In
        amount0Out
        amount1In
        amount1Out
        pair {
            token0Price
            token1Price
        }
        amountUSD
    }
}

"""

FETCH_SPECIFIC_PAIR = """
query FetchSpecificPair($token0_id: ID!, $token1_id: ID!) {
  pair0: pairs(where: {token0: $token0_id, token1: $token1_id}) {
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
    reserve0
    reserve1
  }
  pair1: pairs(where: {token0: $token1_id, token1: $token0_id}) {
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
    reserve0
    reserve1
  }
}

"""

FETCH_SWAPS_TOKEN_IN_TOKEN_OUT = """
query FetchSwapsTokenInTokenOut($token_id: ID!, $start_time: BigInt!, $end_time: BigInt!) {
  swaps1: swaps(
  first: 1
 where: {pair_: {token0: $token_id}, timestamp_lte: $end_time}    
 orderBy: timestamp
    orderDirection: desc
  ) {
      id
        timestamp
        amount0In
        amount0Out
        amount1Out
        amountUSD    
  }
  swaps2: swaps(
  first: 1
 where: {pair_: {token0: $token_id}, timestamp_lte: $end_time}    
    orderBy: timestamp
    orderDirection: desc
  ) {
      id
        timestamp
        amount0In
        amount0Out
        amount1In
        amount1Out
        amountUSD    
  }
}
"""
