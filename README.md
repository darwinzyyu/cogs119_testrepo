## README

# Massive Memory Experiment Project

This project repository is structured to support diverse approaches to running the **Massive Memory Experiment**. Each directory offers a distinct setup, providing flexibility depending on your requirements for experiment data handling and server configuration. Below is an overview of each directory to guide you in selecting the most suitable setup.

## Directory Structure and Purpose

### 1. **Experiment_Draft**

   **Purpose**: This directory contains an initial draft of the experiment designed for the **Project Work: Experiment Draft (Group Submission)** assignment. This draft served as a foundational version of the experiment, enabling essential functionality testing, including image display, memory recall, and structured feedback for incorrect responses.

   - **Core Features**:
      - Manually specified images for memory and test phases within `index.html`
      - Real-time feedback and repetition for incorrect trials, allowing participants to correct errors before advancing
      - Does not incorporate external JSON data, GitHub Gist integration, or automated server setup
   
   - **Use Case**: Ideal for quick testing and prototyping. This setup offers a standalone approach, making it effective for initial experimentation with memory recall and trial handling without additional server or data setup

### 2. **Experiment_using_GitHubGist**

   **Purpose**: This setup leverages GitHub Gist for hosting the experiment’s JSON data file (`stimuli_pairs.json`) to enable remote access to image pairs across all conditions: STATE, EXEMPLAR, and NOVEL. Using GitHub Gist allows for sharing and fetching JSON data via a public raw URL

   - **Core Features**:
      - JSON generation for all experiment conditions, including STATE, EXEMPLAR, and NOVEL, handled in `generating_json.ipynb`
      - External data hosting via GitHub Gist, allowing the experiment to access JSON data directly through a raw URL without a local server
      - **Note**: Manual updates to the Gist are required if the JSON data changes

   - **Use Case**: Optimal for scenarios where remote data access is preferred, especially if the experiment is shared or conducted across various locations. This setup offers flexibility in accessing external data without needing to set up a local server but requires manual maintenance of the Gist content

### 3. **Experiment_using_script**

   **Purpose**: This setup is fully automated, using the `experiment_setup.sh` script to streamline the initialization process. The script facilitates local JSON data generation, server setup, and experiment launch for direct access in a browser

   - **Core Features**:
      - Automation of JSON file generation for all experiment conditions (STATE, EXEMPLAR, and NOVEL)
      - Local server setup through the script, allowing for easy, single-command access to the experiment interface
      - No need for manual data handling or external hosting, as the script handles all dependencies locally

   - **Use Case**: Best suited for local deployment where automation and a self-contained environment are desirable. This setup is recommended for those who prefer a streamlined approach without manual JSON handling or reliance on remote data sources.

## Selection Guide

- **For Prototype Testing**: Use **Experiment_Draft** for a simple, standalone version focused on essential memory and recall mechanics with basic data handling
- **For Remote Data Access**: Use **Experiment_using_GitHubGist** if hosting data externally and accessing it remotely suits your needs. This setup is efficient for shared or distributed experiment setups
- **For Local Automation**: Use **Experiment_using_script** for a fully automated, local setup, especially beneficial if you want minimal manual intervention in starting and running the experiment

Each setup provides a unique approach tailored for different operational requirements. For detailed instructions on each setup, see the individual README files located within each directory. This structure allows you to select and run the Massive Memory Experiment in the way that best aligns with your needs 