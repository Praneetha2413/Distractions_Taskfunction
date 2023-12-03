# Experiment README

## Introduction
In this experiment, participants are divided into four groups, each undertaking 20 trials of a Stroop task. The groups and tasks are as follows:

- **Group 0:** Simple task
- **Group 1:** Simple task with distractions
- **Group 2:** Complex task
- **Group 3:** Complex task with distractions

## Methodology
1. **Stroop Task:** Participants focus on color for the first 10 trials and word for the next 10 in the simple Stroop task.
2. **Complex Stroop Task:** Participants dynamically focus on either the color or the word based on prompts.
3. **Responses:** Participants determine the correct color and press R, G, B on the keyboard for red, green, or blue.
4. **Distractions:**
   - Whatsapp notification background sound
   - Pop-up image notification with sound

5. **Operationalization:**
The primary focus is on measuring task performance, achieved through:
   - **Response Time:** The time taken to respond.
   - **Task Score:** Calculated based on accuracy and speed.

## Folder Structure
The project is organized into the following structure:

- **analysis:**
     Feel free to explore and run the notebooks for detailed analysis.
  - **0_1v2_3.ipynb:** Notebook for comparing Group 0-1 vs. Group 2-3.
  - **0v1.ipynb:** Notebook for analyzing Group 0 vs. Group 1.
  - **2v3.ipynb:** Notebook for analyzing Group 2 vs. Group 3.
  - **form_analysis.ipynb:** Notebook for analyzing form responses.
  - `formresponses.csv` containing form response data.

- **group0, group1, group2, group3:**
  - `stroop00.py`, `stroop0.py`, `stroop10.py`, and `stroop1.py` Python scripts for running the Stroop tasks.
  - CSV files (`01.csv`, `02.csv`, ..., `39.csv`) for each participant's trial data.
  
- **new_design:** Updated Python scripts for the new Stroop task design.

- **utils:** Distraction resources (image and sounds).
  


## Experiment Execution
- Give the Participant an ID to maintain anonymity and use the same ID throughout(both form reponse and Stroop Task). Assign them to a group randomly. 
- Collect the form data & show them the instructions of the task(they are present in 2nd section of the form). Here is the link to the form we have used with duplicatable access:(https://docs.google.com/forms/d/e/1FAIpQLScvQ3Zwvl8Yoc7nUFCDcxGCcD-Xd4iIsQDaVnwgFY6V3GMlIQ/viewform?usp=sharing)
- Replace the current stroop**.py in group folders with the ones from new design and Execute the Python scripts in the group folders for running the Stroop tasks.
- Explore and run the Jupyter notebooks for in-depth analysis.

**Note:** Ensure that the necessary dependencies are installed before running the code.