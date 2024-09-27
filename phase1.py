import requests
import time

class MegaverseAPI:
    BASE_URL = 'https://challenge.crossmint.io/api'

    # Initialize with the candidate ID.
    def __init__(self, candidate_id):
        self.candidate_id = candidate_id

    # Create a Polyanet at the given row and column.
    def create_polyanet(self, row, column):
        url = f'{self.BASE_URL}/polyanets'
        payload = {
            'row': row,
            'column': column,
            'candidateId': self.candidate_id
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Created Polyanet at ({row}, {column})")
        else:
            print(f"Failed to create Polyanet at ({row}, {column}): {response.text}")
            response.raise_for_status()

    # Delete a Polyanet at the given row and column.
    def delete_polyanet(self, row, column):
        url = f'{self.BASE_URL}/polyanets'
        payload = {
            'row': row,
            'column': column,
            'candidateId': self.candidate_id
        }
        response = requests.delete(url, json=payload)
        if response.status_code == 200:
            print(f"Deleted Polyanet at ({row}, {column})")
        else:
            print(f"Failed to delete Polyanet at ({row}, {column}): {response.text}")
            response.raise_for_status()

# Create an X shape with Polyanets on the grid.
def create_x_shape(megaverse_api):
    grid_size = 11  # The grid is 11x11
    for row in range(2, grid_size - 2):
        for column in range(2, grid_size - 2):
            if row == column or row + column == grid_size - 1:  # X-shape condition
                try:
                    megaverse_api.create_polyanet(row, column)
                    time.sleep(0.3)  # Delay to avoid hitting rate limits
                except Exception as e:
                    print(f"Exception occurred at ({row}, {column}): {e}")

# Reset the grid by deleting all Polyanets in the X shape.
def reset_grid(megaverse_api):
    grid_size = 11
    for row in range(grid_size):
        for column in range(grid_size):
            if row == column or row + column == grid_size - 1:
                try:
                    megaverse_api.delete_polyanet(row, column)
                    time.sleep(0.3)
                except Exception as e:
                    print(f"Exception occurred at ({row}, {column}): {e}")

if __name__ == '__main__':
    candidate_id = 'not_sharing_candidate_id_for_security_reasons'  # Candidate ID hidden for security
    megaverse_api = MegaverseAPI(candidate_id)
    reset_grid(megaverse_api)      # Deletes existing Polyanets in the X shape
    create_x_shape(megaverse_api)  # Creates the new X-shaped Polyanet pattern

