## README

# Project Work: Experiment Draft (Group Submission)

This project is a draft of a cognitive science experiment for the "Project Work: Experiment Draft (Group Submission)" assignment. The experiment is designed to present images to participants, test their memory through identification tasks, and handle incorrect responses with trial repetition.

## Purpose

This experiment serves as a preliminary draft to test memory recall and recognition. It focuses on:
- **Memory Phase**: Displaying a series of images for initial viewing
- **Test Phase**: Presenting pairs of images, where participants choose the previously seen image from each pair
- **Incorrect Trial Handling**: Automatically repeating incorrect trials until the correct response is given, providing feedback for each attempt

## Experiment Structure

1. **Memory Phase**:
   - Participants view a set of images one by one, each shown for a fixed duration.
   - Images are displayed with a fixation cross to help participants focus

2. **Test Phase**:
   - Participants are shown pairs of images and must identify the image they saw earlier.
   - If a participant selects the incorrect image, they receive immediate feedback
   - Incorrect trials are added to a queue and repeated at the end of the experiment to ensure that each item is correctly identified

3. **Feedback**:
   - After each selection, feedback is displayed for 1 second
   - The feedback indicates whether the selection was correct or incorrect, helping participants understand their memory performance

## Running the Experiment

1. **Open the `index.html` File**:
   - To begin the experiment, simply open the `index.html` file in a web browser
   - The experiment is configured to run locally without requiring any external server setup

2. **Experiment Flow**:
   - After an introductory screen, the experiment enters fullscreen mode
   - Participants proceed through the memory and test phases, with the experiment automatically tracking and handling incorrect answers

3. **Data Collection**:
   - At the end of the experiment, all collected data is displayed, including participant ID, response accuracy, and trial timing

## Notes

- **Image Set**: The experiment uses six initial images stored in the `stimuli/STATE/USED` and `stimuli/EXEMPLAR/USED` folders
- **Correct and Incorrect Handling**: Incorrect responses are repeated until correctly answered, providing structured feedback for learning and memory reinforcement
- **Experiment Termination**: At the conclusion, participants receive a closing message and are prompted to exit the experiment smoothly

This experiment draft provides a foundational setup for testing memory recall with interactive feedback. Future expansions may include additional images, randomized item selection, and a refined feedback loop for enhanced participant experience. 
