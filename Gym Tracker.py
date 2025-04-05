import tkinter as tk
from tkinter import scrolledtext

#function to save workout
def save_workout():
    exercise = exercise_entry.get()
    muscle = muscle_var,get()
    sets = sets_entry.get()
    reps = reps_entry.get()
    weight = weight_entry.get()

    # Make sure inputs are not empty
    if exercise == "" or sets == "" or reps == "" or weight == "":
        status_label.config(text="❌ Please fill out all fields.")
        return

    try:
        sets = int(sets)
        reps = int(reps)
        weight = float(weight)
    except:
        status_label.config(text="❌ Use numbers for sets, reps, and weight.")
        return

    total = sets * reps * weight

    # Save to file
    with open("workouts.txt", "a") as file:
        file.write(f"{exercise} ({muscle}) - {sets} sets, {reps} reps, {weight} lbs. Total: {total} lbs\n")

    status_label.config(text="✅ Workout saved!")

    # Clear fields
    exercise_entry.delete(0, tk.END)
    sets_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

# Function to show all workouts
def view_workouts():
    workout_box.config(state="normal")
    workout_box.delete(1.0, tk.END)

    try:
        with open("workouts.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                workout_box.insert(tk.END, line)
    except:
        workout_box.insert(tk.END, "No workout history yet.")

    workout_box.config(state="disabled")

# GUI setup
window = tk.Tk()
window.title("Workout Logger")
window.geometry("400x500")

tk.Label(window, text="Exercise Name:").pack()
exercise_entry = tk.Entry(window)
exercise_entry.pack()

tk.Label(window, text="Muscle Group:").pack()
muscle_var = tk.StringVar()
muscle_dropdown = tk.OptionMenu(window, muscle_var, "Chest", "Back", "Biceps", "Triceps", "Legs")
muscle_dropdown.pack()
muscle_var.set("Chest")  # Default

tk.Label(window, text="Sets:").pack()
sets_entry = tk.Entry(window)
sets_entry.pack()

tk.Label(window, text="Reps:").pack()
reps_entry = tk.Entry(window)
reps_entry.pack()

tk.Label(window, text="Weight (lbs):").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Button(window, text="Save Workout", command=save_workout).pack(pady=5)
tk.Button(window, text="View Workouts", command=view_workouts).pack(pady=5)

status_label = tk.Label(window, text="")
status_label.pack()

workout_box = scrolledtext.ScrolledText(window, width=40, height=10, state="disabled")
workout_box.pack(pady=10)

window.mainloop()