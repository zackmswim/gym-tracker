import tkinter as tk
from tkinter import scrolledtext
import os  # Needed to check if file exists

# Function to save a workout
def save_workout():
    exercise = exercise_entry.get()
    sets = sets_entry.get()
    reps = reps_entry.get()
    weight = weight_entry.get()
    
    # Check if all fields are filled
    if not exercise or not sets or not reps or not weight:
        status_label.config(text="❌ Please fill in all fields!", fg="red")
        return
    
    try:
        sets = int(sets)
        reps = int(reps)
        weight = float(weight)
    except ValueError:
        status_label.config(text="❌ Sets & Reps must be whole numbers, Weight must be a number!", fg="red")
        return

    total_volume = sets * reps * weight  # Calculate total volume

    # Save to file
    with open("workouts.txt", "a") as file:
        file.write(f"{exercise} - {sets} sets, {reps} reps, {weight} lbs (Total: {total_volume} lbs)\n")

    # Show success message
    status_label.config(text=f"✅ Workout Saved! Total: {total_volume} lbs", fg="green")

    # Clear input fields
    exercise_entry.delete(0, tk.END)
    sets_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

# Function to load and display past workouts
def view_workouts():
    if not os.path.exists("workouts.txt"):  # Check if file exists
        workouts_text.config(state="normal")
        workouts_text.delete(1.0, tk.END)
        workouts_text.insert(tk.END, "❌ No workout history found!\n")
        workouts_text.config(state="disabled")
        return
    
    with open("workouts.txt", "r") as file:
        workouts = file.readlines()  # Read all lines from the file

    workouts_text.config(state="normal")  # Allow editing
    workouts_text.delete(1.0, tk.END)  # Clear previous text

    if not workouts:
        workouts_text.insert(tk.END, "❌ No workouts logged yet!\n")
    else:
        workouts_text.insert(tk.END, "".join(workouts))

    workouts_text.config(state="disabled")  # Disable editing again

# Create GUI window
root = tk.Tk()
root.title("Gym Strength Tracker")
root.geometry("500x500")
root.configure(bg="#f0f0f0")  # Light gray background

# Header Label
header_label = tk.Label(root, text="🏋️ Gym Strength Tracker", font=("Arial", 16, "bold"), bg="#f0f0f0")
header_label.pack(pady=10)

# Input Frame (Better Organization)
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=5)

# Labels and input fields
tk.Label(input_frame, text="Exercise Name:", bg="#f0f0f0").grid(row=0, column=0, sticky="e", padx=5, pady=2)
exercise_entry = tk.Entry(input_frame, width=20)
exercise_entry.grid(row=0, column=1, pady=2)

tk.Label(input_frame, text="Number of Sets:", bg="#f0f0f0").grid(row=1, column=0, sticky="e", padx=5, pady=2)
sets_entry = tk.Entry(input_frame, width=20)
sets_entry.grid(row=1, column=1, pady=2)

tk.Label(input_frame, text="Reps per Set:", bg="#f0f0f0").grid(row=2, column=0, sticky="e", padx=5, pady=2)
reps_entry = tk.Entry(input_frame, width=20)
reps_entry.grid(row=2, column=1, pady=2)

tk.Label(input_frame, text="Weight per Set (lbs):", bg="#f0f0f0").grid(row=3, column=0, sticky="e", padx=5, pady=2)
weight_entry = tk.Entry(input_frame, width=20)
weight_entry.grid(row=3, column=1, pady=2)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=5)

save_button = tk.Button(button_frame, text="💾 Save Workout", command=save_workout, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
save_button.grid(row=0, column=0, padx=5, pady=5)

view_button = tk.Button(button_frame, text="📜 View Workouts", command=view_workouts, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
view_button.grid(row=0, column=1, padx=5, pady=5)

# Status label (for save confirmation)
status_label = tk.Label(root, text="", fg="black", bg="#f0f0f0", font=("Arial", 10, "bold"))
status_label.pack()

# Scrollable Text Box for Workout History
workouts_text = scrolledtext.ScrolledText(root, width=50, height=10, state="disabled", font=("Arial", 10))
workouts_text.pack(pady=10)

# Run the GUI
root.mainloop()
