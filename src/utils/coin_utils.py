import json
import os

def find_coin_id_by_symbol(target_symbol):
    # Get the absolute path from the relative path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_relative_path="coins_list.json"
    json_file_path = os.path.join(current_dir, json_file_relative_path)
    
    with open(json_file_path, 'r') as f:
        json_data = json.load(f)
        
    target_symbol = target_symbol.lower()
    
    for coin in json_data:
        if coin["symbol"].lower() == target_symbol:
            return coin["id"]
            
    return None  # Return None if the symbol is not found

