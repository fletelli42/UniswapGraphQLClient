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


# Add more GraphQL queries as needed.
