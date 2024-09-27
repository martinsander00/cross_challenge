import requests
import time

class MegaverseAPI:
    BASE_URL = 'https://challenge.crossmint.io/api'

    # Initialize with candidate ID.
    def __init__(self, candidate_id):
        self.candidate_id = candidate_id

    # Create a Polyanet at a specific position.
    def create_polyanet(self, row, column):
        url = f'{self.BASE_URL}/polyanets'
        payload = {
            'row': row,
            'column': column,
            'candidateId': self.candidate_id
        }
        response = requests.post(url, json=payload)
        self.handle_response(response, 'Polyanet', 'create', row, column)

    # Delete a Polyanet at a specific position.
    def delete_polyanet(self, row, column):
        url = f'{self.BASE_URL}/polyanets'
        payload = {
            'row': row,
            'column': column,
            'candidateId': self.candidate_id
        }
        response = requests.delete(url, json=payload)
        self.handle_response(response, 'Polyanet', 'delete', row, column)

    # Create a Soloon of a given color.
    def create_soloon(self, row, column, color):
        url = f'{self.BASE_URL}/soloons'
        payload = {
            'row': row,
            'column': column,
            'color': color.lower(),
            'candidateId': self.candidate_id
        }
        response = requests.post(url, json=payload)
        self.handle_response(response, f'{color.capitalize()} Soloon', 'create', row, column)

    # Delete a Soloon at a specific position.
    def delete_soloon(self, row, column):
        url = f'{self.BASE_URL}/soloons'
        payload = {
            'row': row,
            'column': column,
            'candidateId': self.candidate_id
        }
        response = requests.delete(url, json=payload)
        self.handle_response(response, 'Soloon', 'delete', row, column)

    # Create a Cometh in a given direction.
    def create_cometh(self, row, column, direction):
        url = f'{self.BASE_URL}/comeths'
        payload = {
            'row': row,
            'column': column,
            'direction': direction.lower(),
            'candidateId': self.candidate_id
        }
        response = requests.post(url, json=payload)
        self.handle_response(response, f'{direction.capitalize()} Cometh', 'create', row, column)

    # Delete a Cometh at a specific position.
    def delete_cometh(self, row, column):
        url = f'{self.BASE_URL}/comeths'
        payload = {
            'row': row,
            'column': column,
            'candidateId': self.candidate_id
        }
        response = requests.delete(url, json=payload)
        self.handle_response(response, 'Cometh', 'delete', row, column)

    # Handle API response, print success or failure.
    def handle_response(self, response, object_type, action, row, column):
        if response.status_code == 200:
            print(f"{action.capitalize()}d {object_type} at ({row}, {column})")
        else:
            print(f"Failed to {action} {object_type} at ({row}, {column}): {response.text}")
            response.raise_for_status()

    # Fetch the goal map from the API.
    def fetch_goal_map(self):
        url = f'{self.BASE_URL}/map/{self.candidate_id}/goal'
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfully fetched the goal map.")
            return response.json()
        else:
            print(f"Failed to fetch goal map: {response.text}")
            response.raise_for_status()

# Parse the goal map to extract grid information.
def parse_goal_map(goal_map):
    return goal_map.get('goal', [])

# Map symbols to astral object types (Polyanet, Soloon, Cometh) and their attributes.
def map_symbol_to_astral_object(symbol):
    symbol = symbol.lower()
    if symbol == 'polyanet':
        return 'polyanet', None
    elif 'soloon' in symbol:
        color = symbol.split('_')[0]
        return 'soloon', color
    elif 'cometh' in symbol:
        direction = symbol.split('_')[0]
        return 'cometh', direction
    else:
        return None, None  # Empty space or unknown symbol

# Create astral objects based on the goal map.
def create_megaverse(megaverse_api, goal_grid):
    for row_index, row in enumerate(goal_grid):
        for col_index, symbol in enumerate(row):
            object_type, attribute = map_symbol_to_astral_object(symbol)
            if object_type == 'polyanet':
                try:
                    megaverse_api.create_polyanet(row_index, col_index)
                    time.sleep(0.5)  # Delay to avoid rate limits
                except Exception as e:
                    print(f"Error creating Polyanet at ({row_index}, {col_index}): {e}")
            elif object_type == 'soloon':
                try:
                    megaverse_api.create_soloon(row_index, col_index, attribute)
                    time.sleep(0.5)
                except Exception as e:
                    print(f"Error creating {attribute.capitalize()} Soloon at ({row_index}, {col_index}): {e}")
            elif object_type == 'cometh':
                try:
                    megaverse_api.create_cometh(row_index, col_index, attribute)
                    time.sleep(0.5)
                except Exception as e:
                    print(f"Error creating {attribute.capitalize()} Cometh at ({row_index}, {col_index}): {e}")

# Reset the entire grid by attempting to delete any existing objects.
def reset_megaverse(megaverse_api, grid_rows, grid_cols):
    for row in range(grid_rows):
        for col in range(grid_cols):
            try:
                megaverse_api.delete_polyanet(row, col)
                time.sleep(0.5)
            except:
                pass
            try:
                megaverse_api.delete_soloon(row, col)
                time.sleep(0.5)
            except:
                pass
            try:
                megaverse_api.delete_cometh(row, col)
                time.sleep(0.5)
            except:
                pass

if __name__ == '__main__':
    candidate_id = 'not_sharing_candidate_id_for_security_reasons'  # Candidate ID omitted for security
    megaverse_api = MegaverseAPI(candidate_id)

    # Fetch and parse the goal map
    goal_map_data = megaverse_api.fetch_goal_map()
    goal_grid = parse_goal_map(goal_map_data)
    grid_rows = len(goal_grid)
    grid_cols = len(goal_grid[0]) if grid_rows > 0 else 0

    # Reset the megaverse grid (uncomment to enable)
    # reset_megaverse(megaverse_api, grid_rows, grid_cols)

    # Create the megaverse according to the goal map
    create_megaverse(megaverse_api, goal_grid)

