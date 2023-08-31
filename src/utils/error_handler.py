# utils/error_handler.py

class UniswapError(Exception):
    """
    Custom exception class for Uniswap-related errors
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

        
def handle_api_error(response):
    """
    Checks the API response for errors and raises a UniswapError if any are found.
    """
    if response.status_code != 200:
        raise UniswapError(f"API Error: Received status code {response.status_code}")

    data = response.json()
    if "errors" in data:
        raise UniswapError(f"API Error: {data['errors']}")


def handle_value_error(value, expected_type):
    """
    Raises a UniswapError if the value is not of the expected type.
    """
    if not isinstance(value, expected_type):
        raise UniswapError(f"Value Error: Expected {expected_type}, got {type(value)}")
