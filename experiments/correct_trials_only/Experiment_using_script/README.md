## README

# Experiment Setup and Execution

This project is designed to set up and run a cognitive science experiment for the Massive Memory Experiment using the `experiment_setup.sh` script. The script handles converting the Jupyter notebook for JSON generation, setting up a local server, and opening the experiment in your default browser.

## Script Overview

### `experiment_setup.sh`

The `experiment_setup.sh` script automates the following steps:
1. **Convert Notebook to Script**: Converts the `generating_json.ipynb` Jupyter notebook into a Python script `generating_json.py`
2. **JSON Generation**: Executes `generating_json.py` to generate `novel_pairs.json` and `stimuli_pairs.json` files, which contain image pairing data required for the experiment
3. **Local Server Setup**: Starts a local HTTP server to serve the experiment files
4. **Experiment Launch**: Opens `index.html` in your default browser to begin the experiment

## Requirements

- **Python 3**: Ensure Python 3 is installed on your system
- **Jupyter Notebook** (optional): Required only if you need to manually edit and convert `generating_json.ipynb`. Alternatively, you can work directly with `generating_json.py` if you prefer editing in **Visual Studio Code**.

## Using Visual Studio Code (VS Code)

If you’re working with Visual Studio Code, ensure the following:
- You can edit `generating_json.py` directly in VS Code. The script `experiment_setup.sh` does not require any additional Jupyter setup if you’re editing in VS Code
- Simply run `experiment_setup.sh` as detailed below, which will execute `generating_json.py` to generate the required JSON files

## How to Run

1. **Make the script executable (if not already)**:
   ```bash
   chmod +x experiment_setup.sh
   ```

2. **Run the script**:
   ```bash
   ./experiment_setup.sh
   ```

3. **Access the experiment**: The script will open the experiment in your default browser at `http://localhost:8000/index.html`. If it doesn't open automatically, manually navigate to:
   ```
   http://localhost:8000/index.html
   ```

4. **Terminate the server**: When finished, stop the server by pressing `Ctrl+C` in the terminal running the script
