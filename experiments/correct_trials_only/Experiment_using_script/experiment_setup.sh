#!/bin/bash

# 1. Generate `novel_pairs.json` and `stimuli_pairs.json` files by executing the notebook
echo "Generating JSON files from Jupyter notebook..."
jupyter nbconvert --to notebook --execute generating_json.ipynb --output executed_generating_json.ipynb

# Check if the files were created successfully
if [[ ! -f "stimuli_pairs.json" || ! -f "novel_pairs.json" ]]; then
  echo "Error: Failed to generate stimuli files."
  exit 1
fi
echo "JSON files generated."

# 2. Start a local server using Python's HTTP server module
echo "Starting local server on http://localhost:8000..."
python3 -m http.server 8000 &  # Start server in the background
SERVER_PID=$!  # Store the server's process ID to terminate it later

# 3. Open the experiment in the default browser
sleep 2  # Give the server a moment to start
open "http://localhost:8000/index.html" || echo "Please open http://localhost:8000/index.html in your browser."

# Wait for the user to terminate the script manually to keep the server running
echo "Press Ctrl+C to stop the server."
trap "kill $SERVER_PID" SIGINT  # Kill server on script exit
wait $SERVER_PID
