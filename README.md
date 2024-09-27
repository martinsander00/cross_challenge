# Megaverse Challenge

## Overview
This script interacts with the Megaverse API, allowing the user to create or delete Polyanet objects in an 11x11 grid. The goal is to form an X-shape pattern using Polyanets by sending requests to the API. Second phase involved a more complicated version of phase 1.

## Requirements
- Python 3.x
- `requests` library (install via `pip install requests`)
- A valid `candidate_id` (replace the placeholder in the code with the correct one)

## How to Use

1. **Install dependencies:**
   Make sure you have the `requests` library installed. If not, run:

```bash
pip install requests
```

2. **Set up your `candidate_id`:**
Replace the placeholder `not_sharing_candidate_id_for_security_reasons` in the code with your actual candidate ID.

3. **Run the Script:**
You can run the script to first reset the grid and then create an X-shape pattern by executing:

```bash
python phase1.py
python phase2.py
```

Make sure you use the correct version of Python and pip.

## Functions

- `create_polyanet(row, column)`: Creates a Polyanet at the specified coordinates in the grid.
- `delete_polyanet(row, column)`: Deletes a Polyanet at the specified coordinates in the grid.
- `create_x_shape(megaverse_api)`: Creates an X-shape pattern by placing Polyanets in the correct positions in the grid.
- `reset_grid(megaverse_api)`: Deletes all Polyanets in the X-shape pattern in case you want to start fresh.

## Notes

- There is a small delay (`time.sleep(0.3)`) between API requests to avoid hitting rate limits.
