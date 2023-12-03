import tkinter as tk
from tkinter.simpledialog import askstring
import random
import time
import csv
from PIL import Image, ImageTk

# Take participant name as input in the terminal
participant_name = input("Please enter your ID(ask the experimenters): ")

root = tk.Tk()
root.title("Stroop Experiment")

# Define some colors and color names
colors = ['red', 'green', 'blue']
color_names = ['RED', 'GREEN', 'BLUE']
color_names_1 = ['RED', 'GREEN', 'BLUE']

# Experiment variables
total_trials = 20  # Total number of trials
current_trial = 0
total_responses = 0
correct_responses = []
start_time = 0
response_times = []  # List to store response times


# CSV file setup
csv_filename = f"{participant_name}.csv"
csv_header = ["Trial", "Correct", "Response Time (s)"]

def display_color_word():
    global current_trial, start_time
    if current_trial < total_trials:
        color_label.config(text="")
        prompt = random.choice(["Focus on COLOR", "Focus on WORD"])
        prompt_label.config(text=prompt)
        nextpromt_label.config(text=f" Up Next: TRIAL {current_trial + 1} ")
        root.update()
        time.sleep(1.5)
        nextpromt_label.config(text="")
        prompt_label.config(text="")

        start_time = time.time()  # Record the start time of displaying the word

        # Randomly select a color and a corresponding text
        color_index = random.randint(0, len(colors) - 1)
        display_color = colors[color_index]

        # Shuffle the color names to display incongruent words and colors
        random.shuffle(color_names)
        display_name = color_names[0]

        # Update the label with the prompt and the color word
        color_label.config(text=display_name, fg=display_color)
        root.bind('<KeyPress>', lambda event: check_response(event, prompt))

        current_trial += 1

    else:
        print("Experiment finished. Total trials completed.")
        save_to_csv()
        root.quit()  # Close the tkinter window
def save_to_csv():
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csv_header)
        for i in range(total_trials):
            row_data = [
                i + 1,
                correct_responses[i] if i < len(correct_responses) else '',
                response_times[i] if i < len(response_times) else ''
            ]
            writer.writerow(row_data)


def check_response(event, prompt):
    global total_responses, correct_responses, start_time

    pressed_key = event.char.upper()

    if prompt == "Focus on COLOR":
        # Condition 1: Focus on COLOR
        if pressed_key in ['R', 'G', 'B']:
            total_responses += 1
            response_time = time.time() - start_time
            response_times.append(response_time)  # Store response time for this trial

            # Get the index of the pressed key (R, G, B)
            key_index = ['R', 'G', 'B'].index(pressed_key)

            # Check if the pressed key corresponds to the displayed ink color
            displayed_color = color_label.cget("fg")
     
            if displayed_color == colors[key_index]:
                correct_responses.append(1)
                print(f"Trial {current_trial}: Correct! Response time: {response_time:.2f} seconds")
            else:
                correct_responses.append(0)
                print(f"Trial {current_trial}: Incorrect. Response time: {response_time:.2f} seconds")

            # Unbind keypress and display the next word or finish the experiment
            root.unbind('<KeyPress>')
            display_color_word()
        else:
            print("Invalid key pressed. Please press R, G, or B.")

    elif prompt == "Focus on WORD":
        # Condition 2: Focus on WORD
        if pressed_key in ['R', 'G', 'B']:
            total_responses += 1
            response_time = time.time() - start_time
            response_times.append(response_time)  # Store response time for this trial

            # Get the index of the pressed key (R, G, B)
            key_index = ['R', 'G', 'B'].index(pressed_key)

            # Check if the pressed key corresponds to the displayed word
            displayed_name = color_label.cget("text").upper()
      
            if displayed_name == color_names_1[key_index]:
                correct_responses.append(1)

                print(f"Trial {current_trial}: Correct! Response time: {response_time:.2f} seconds")
            else:
                correct_responses.append(0)
                print(f"Trial {current_trial}: Incorrect. Response time: {response_time:.2f} seconds")

            # Unbind keypress and display the next word or finish the experiment
            root.unbind('<KeyPress>')
            display_color_word()
        else:
            print("Invalid key pressed. Please press R, G, or B.")

    else:
        # Any other response is considered incorrect
        print("Incorrect prompt. Please check the prompt message.")

root.geometry("1920x1280")
nextpromt_label = tk.Label(root, text='', font=('Helvetica', 40), justify='center', fg='black')
nextpromt_label.pack(pady=100)



# Create a label to display the prompt
prompt_label = tk.Label(root, text='', font=('Helvetica', 40), fg='black')
prompt_label.pack(pady = 20)

# Create a label to display the color word
color_label = tk.Label(root, text='', font=('Helvetica', 50), justify='center')
color_label.pack()

# Create a label for the notification
notification_label = tk.Label(root)
notification_label.pack()

# Display the initial color word
display_color_word()

# Set the window size

root.mainloop()
