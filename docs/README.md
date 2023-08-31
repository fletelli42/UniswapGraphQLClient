
# UniswapGraphQLClient

UniswapGraphQLClient is a Python library designed to interact with the Uniswap V2 and V3 subgraphs via GraphQL. This project provides an API client to fetch information about tokens, pairs, and swap transactions from Uniswap. It also includes utility functions for data conversions and metrics calculation.

## Features
- Fetch token details by contract address for V2 and V3
- Retrieve pairs involving a particular token for V2 and V3
- Get swap transactions for a specific pair for V2 and V3
- Utility functions for data conversion and error handling
- Paginated data fetching
- Real-time data updater service
- Support for Uniswap V3 queries and metrics

## Table of Contents
1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Tests](#tests)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

Clone the repository:

```bash
git clone https://github.com/your_username/UniswapGraphQLClient.git
cd UniswapGraphQLClient
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Alternatively, run the setup file to install the package:

```bash
python setup.py install
```

## Usage

### Uniswap V2

Here is an example code snippet on how to use the V2 library:


```python
from api.client import UniswapClient

client = UniswapClient()

# Fetch token information
token_data = client.fetch_token('0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984')
print(f"Token Data: {token_data}")

# Fetch pairs for a specific token
pairs = client.fetch_pairs_for_token('0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984')
print(f"Pairs: {pairs}")
```


### Uniswap V3

Here is an example code snippet on how to use the V3 library:

```python
from api.client_v3 import UniswapV3Client

client = UniswapV3Client()

# Fetch token information
token_data = client.fetch_token('0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984')
print(f"Token Data: {token_data}")

# Fetch pairs for a specific token
pairs = client.fetch_pairs_for_token('0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984')
print(f"Pairs: {pairs}")
```

For more examples, please refer to the `main.py` and `mainv3.py` files.

## Tests

To run the tests, navigate to the project directory and run:

```bash
python -m unittest discover tests
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

MIT

---
For more details on each part of the code, please refer to the comments and documentation in the respective files. Feel free to contribute and make any improvements.
