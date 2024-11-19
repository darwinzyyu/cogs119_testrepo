## README

### Overview

This README provides instructions for generating JSON files used in the **Massive Memory Experiment** and outlines the steps for uploading `stimuli_pairs.json` to a GitHub Gist to make it accessible via a raw URL

### Steps for JSON File Generation and GitHub Gist Setup

#### Step 1: Generate JSON Files

1. Open `generating_json.ipynb` in either Jupyter Notebook or Visual Studio Code
2. Execute all code cells to generate the JSON files `novel_pairs.json` and `stimuli_pairs.json`

**Note**: After generating these files, open **`stimuli_pairs.json`**, copy its content, and proceed to the GitHub Gist setup outlined below. If `stimuli_pairs.json` content changes or is regenerated, you must repeat this step to manually update the Gist

#### Step 2: Create a GitHub Gist

1. Go to [GitHub Gist](https://gist.github.com/) and log in
2. Click on **"Create a new gist"**
3. **Fill in the following fields**:
   - **Description**: Enter `JSON file for Massive Memory Experiment stimuli: STATE, EXEMPLAR, and NOVEL conditions`
   - **File Name**: Set this to `massive_memory_stimuli.json`
   - **File Content**: Paste the content copied from `stimuli_pairs.json`

4. Click **"Create public gist"**.

#### Step 3: Get the Raw URL

After creating the Gist, follow these steps to obtain the raw URL, which will be used to access the JSON data in the experiment code:

1. Copy the Gist URL displayed on the page (e.g., `https://gist.github.com/NeuraByte-UCSD-ITS/b55ceb222e8f3e23a13d48db5283bb5e`)
2. Modify this URL to convert it into the raw URL as follows:
   - Replace `gist.github.com` with `gist.githubusercontent.com`
   - Append `/raw` after the unique identifier

   The final raw URL should look like this:
   ```
   https://gist.githubusercontent.com/NeuraByte-UCSD-ITS/b55ceb222e8f3e23a13d48db5283bb5e/raw/massive_memory_stimuli.json
   ```

### Important Notes

- **Manual Update Requirement**: If the content of `stimuli_pairs.json` changes, repeat Step 2 to update the Gist with the new content
- **Raw URL Usage**: Use the raw URL to access the JSON data directly in your experiment setup.
- **`stimuli_pairs.json`**: This file contains stimuli pairs for **EXEMPLAR** and **STATE** conditions and is directly used in the experiment setup
- **`novel_pairs.json`**: This file holds image pairs for the **NOVEL** condition, which is structured differently from EXEMPLAR and STATE. While `novel_pairs.json` is generated, it is **not directly used** in the experiment. The unique setup of the NOVEL condition necessitates a different approach, and this file is primarily for reference. If you need `novel_pairs.json` in future setups, you would manually handle it accordingly.