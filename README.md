# Hypixel Skyblock Bazaar Automation

This project is designed to interact with the Hypixel Skyblock API to gather and analyze bazaar data. It provides functionalities to fetch player statistics, retrieve bazaar prices, compare prices, and automate data collection and analysis.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality Overview](#functionality-overview)
- [Dependencies](#dependencies)

## Features

- Inspect player stats using their UUID.
- Retrieve and export bazaar price data.
- Automatically collect bazaar data every hour.
- Analyze average buy/sell prices and profit margins.
- Generate JSON and text files for record-keeping.

## Installation

To use this project, you need to install the required Python libraries. You can do this using `pip`. Run the following command in your terminal:

```bash
pip install requests pandas mojang
```

## Usage
1. Clone the repository:
```bash
git clone https://github.com/yourusername/hypixel-skyblock-bazaar-automation.git
```
2. Navigate into the project directory:
```bash
cd hypixel-skyblock-bazaar-automation
```
3. Run the main program:
```bash
python main.py
```

## Functionality Overview

### Main Program (`main.py`)

- **Imports**:
    - `from definitions import *`: Imports all functions defined in the `definitions.py` file.
    - `from time import sleep`: Provides the ability to pause execution for a specified duration. (for debug only)
    - `import schedule`: Allows for scheduling tasks such as periodic data fetching. (for debug only)
    - `import time`: Provides various time-related functionalities.

- **Main Loop**: The program prompts the user to choose from the following actions:
    - **Inspect Player Stats (`I`)**: Enter a player's UUID to retrieve their achievement statistics.
    - **Retrieve Bazaar Reference Prices (`R`)**: Fetch current bazaar prices for items and store them in a reference file.
    - **Compare Bazaar Prices (`C`)**: Analyze the difference between buy and sell prices for specific items.
    - **Enable Automatic Mode (`A`)**: Activate a scheduled process to automatically gather bazaar data every hour.

### Functions in `definitions.py`

1. **`getBazaarInfos(lien)`**: Retrieves real-time bazaar information from the API.
2. **`getPlayerInfos(clef_API, UUID)`**: Fetches player statistics using their unique UUID and an API key.
3. **`printPlayerInfo(player_info_uuid)`**: Displays the player's achievements and stats in a user-friendly format.
4. **`data_ref(lien)`**: Creates a reference file containing the current bazaar prices for various items.
5. **`data_comp(lien)`**: Generates a comparison file to analyze differences in bazaar prices over time.
6. **`data_comp_auto()`**: Automatically compiles and updates bazaar data by fetching new entries every hour.
7. **`recup_data_comp()`**: Collects comparison data and saves it to a text file for easy access.
8. **`recup_data_comp_auto()`**: Gathers, organizes, and manages JSON data for automated comparisons.
9. **`recup_data_ref()`**: Retrieves and formats reference data, writing it to a text file for record-keeping.
10. **`moyenne_par_item()`**: Calculates average prices and potential profits for items based on historical data.
11. **`comparer_prix_achat_vente()`**: Compares current buy prices with historical average sell prices to identify profit opportunities.
12. **`verifier_et_creer_dossier(chemin)`**: Checks if specified directories exist and creates them if they do not.
13. **`flip(lien)`**: Analyzes bazaar opportunities for flipping items based on price differences.
14. **`data_get_hourly(lien)`**: Fetches bazaar data on an hourly basis, storing it in JSON files for later analysis.
15. **`full_auto(lien)`**: Automates the entire process of data collection, analysis, and record-keeping without user intervention.

## Dependencies

To run this project, you need to install the following Python packages:

1. **`schedule`**: For scheduling tasks and automating data fetching.
   - Installation: 
     ```bash
     pip install schedule
     ```

2. **`requests`**: For making HTTP requests to the APIs.
   - Installation: 
     ```bash
     pip install requests
     ```

3. **`json`**: This is included in Python's standard library, so no installation is needed.
